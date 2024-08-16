from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from config import CONFIG

def initialize_llm(model_name=None):
    model_name = model_name or CONFIG['default_model']
    return ChatGroq(
        groq_api_key=CONFIG['groq_api_key'],
        model_name=model_name,
        temperature=CONFIG['temperature'],
        max_tokens=CONFIG['max_tokens']
    )

llm = initialize_llm()

# RAG prompt
rag_prompt = ChatPromptTemplate.from_template("""
다음 컨텍스트를 바탕으로 질문에 답변하세요:
{context}

질문: {question}

답변을 한국어로 제공해 주세요.
""")

# RAG chain
def create_rag_chain():
    global llm
    rag_chain = (
        {"context": lambda x: x["context"], "question": lambda x: x["question"]}
        | rag_prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain

rag_chain = create_rag_chain()

def change_model(model_name):
    global llm, rag_chain
    llm = initialize_llm(model_name)
    rag_chain = create_rag_chain()
    return f"Model changed to {model_name}"

def process_with_rag(question, context):
    return rag_chain.invoke({"question": question, "context": context})