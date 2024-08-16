import gradio as gr
from config import CONFIG
from src.llm.model import change_model, process_with_rag
from src.vector_db.chroma_db import similarity_search
from src.utils.file_utils import add_file, get_file_list, initialize_files
from src.document_processor.document_processor import SUPPORTED_EXTENSIONS
import asyncio


async def process_message(message, history):
    context = similarity_search(message)
    response = process_with_rag(message, context)
    return response


async def type_message(message, delay=0.0005):
    for i in range(len(message) + 1):
        yield message[:i]
        await asyncio.sleep(delay)


def create_interface():
    with gr.Blocks() as demo:
        gr.Markdown("# 🌀 Simple RAG")
        gr.Markdown("This program uses Retrieval-Augmented Generation to answer questions based on uploaded PDF "
                    "documents. It combines information retrieval with language generation to provide accurate and "
                    "context-aware responses.")

        with gr.Row():
            with gr.Column(scale=3):
                chatbot = gr.Chatbot(
                    [],
                    elem_id="chatbot",
                    avatar_images=("asset/images/user.png", "asset/images/chatbot.png"),
                    bubble_full_width=False,
                    height=400
                )
                msg = gr.Textbox(show_label=False, placeholder="Enter your message...")
                clear = gr.ClearButton([msg, chatbot])

            with gr.Column(scale=1):
                model_dropdown = gr.Dropdown(choices=CONFIG['llm_models'],
                                             value=CONFIG['default_model'],
                                             label="Select LLM Model")
                model_status = gr.Markdown("Current Model: " + CONFIG['default_model'])

                with gr.Tabs():
                    with gr.TabItem("Current Files"):
                        file_output = gr.Textbox(label="Current Files")
                    with gr.TabItem("Upload Status"):
                        upload_status = gr.Textbox(label="Upload Status")

                file_upload = gr.File(label=f"Drop files here (Supported: {', '.join(SUPPORTED_EXTENSIONS)})",
                                      file_types=list(SUPPORTED_EXTENSIONS))

        async def respond(message, chat_history):
            bot_message = await process_message(message, chat_history)
            chat_history.append((message, ""))
            async for partial_message in type_message(bot_message):
                chat_history[-1] = (message, partial_message)
                yield "", chat_history, get_file_list()

        def handle_file_upload(file):
            status, _, file_list = add_file(file)
            return status, file_list, None  # None을 반환하여 file_upload를 초기화

        msg.submit(respond, [msg, chatbot], [msg, chatbot, file_output])
        file_upload.upload(handle_file_upload, file_upload, [upload_status, file_output, file_upload])
        model_dropdown.change(change_model, model_dropdown, model_status)

        demo.load(initialize_files, outputs=file_output)

    return demo


def launch_interface():
    demo = create_interface()
    demo.launch()