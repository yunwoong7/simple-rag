from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from config import CONFIG


embeddings = OpenAIEmbeddings(openai_api_key=CONFIG['openai_api_key'])

def initialize_vector_db():
    return Chroma(persist_directory=CONFIG['vector_db_path'], embedding_function=embeddings)

vectorstore = initialize_vector_db()

def add_documents(documents):
    vectorstore.add_documents(documents)

def similarity_search(query):
    return vectorstore.similarity_search(query)