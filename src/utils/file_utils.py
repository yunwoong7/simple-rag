import os
import shutil
from config import CONFIG
from src.vector_db.chroma_db import add_documents
from src.document_processor.document_processor import process_document, is_supported_file, SUPPORTED_EXTENSIONS

current_files = []


def get_file_list():
    return ", ".join(current_files) if current_files else "No documents found"


def add_file(file):
    global current_files
    if file is None:
        return "No file uploaded.", None, get_file_list()

    file_path = file.name
    if not is_supported_file(file_path):
        return f"Unsupported file type. Supported types are: {', '.join(SUPPORTED_EXTENSIONS)}", None, get_file_list()

    try:
        # 파일 복사
        destination = os.path.join(CONFIG['data_dir'], os.path.basename(file_path))
        shutil.copy(file_path, destination)

        # 문서 처리 및 벡터 저장소에 추가
        documents = process_document(destination)
        add_documents(documents)

        # 현재 파일 목록에 추가
        file_name = os.path.basename(file_path)
        if file_name not in current_files:
            current_files.append(file_name)

        return f"File {file_name} added and processed successfully.", None, get_file_list()
    except Exception as e:
        error_msg = f"Error processing {os.path.basename(file_path)}: {str(e)}"
        print(error_msg)  # 콘솔에 오류 출력
        return error_msg, None, get_file_list()


def initialize_files():
    global current_files
    data_dir = CONFIG['data_dir']
    current_files = [f for f in os.listdir(data_dir) if is_supported_file(f) and not f.startswith('.')]

    for file in current_files:
        file_path = os.path.join(data_dir, file)
        try:
            documents = process_document(file_path)
            add_documents(documents)
            print(f"Processed and added {file} to the vector store.")
        except Exception as e:
            print(f"Error processing {file}: {str(e)}")
            current_files.remove(file)  # 처리에 실패한 파일은 목록에서 제거

    return get_file_list()
