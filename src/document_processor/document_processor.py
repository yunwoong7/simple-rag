from langchain_community.document_loaders import (
    PyPDFLoader,
    UnstructuredFileLoader,
    UnstructuredExcelLoader,
    UnstructuredMarkdownLoader,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CONFIG

SUPPORTED_EXTENSIONS = ('.pdf', '.txt', '.xlsx', '.xls', '.md', '.markdown')

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CONFIG['chunk_size'],
    chunk_overlap=CONFIG['chunk_overlap']
)

def get_loader_for_file(file_path):
    if file_path.lower().endswith('.pdf'):
        return PyPDFLoader(file_path)
    elif file_path.lower().endswith('.txt'):
        return UnstructuredFileLoader(file_path)
    elif file_path.lower().endswith(('.xlsx', '.xls')):
        return UnstructuredExcelLoader(file_path)
    elif file_path.lower().endswith(('.md', '.markdown')):
        return UnstructuredMarkdownLoader(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")

def process_document(file_path):
    loader = get_loader_for_file(file_path)
    documents = loader.load()
    return text_splitter.split_documents(documents)

def is_supported_file(file_path):
    return file_path.lower().endswith(SUPPORTED_EXTENSIONS)