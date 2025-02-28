import chromadb
from langchain.vectorstores import Chroma
from langchain.embeddings import GoogleGenerativeAIEmbeddings
from config import GEMINI_API_KEY

chroma_client = chromadb.PersistentClient(path="db/")

def add_document(text):
    collection = chroma_client.get_or_create_collection(name="app_info")
    collection.add(ids=[str(len(collection.get()["ids"])+1)], documents=[text])
    return "Document added successfully."

def search_document(query):
    collection = chroma_client.get_or_create_collection(name="app_info")
    docs = collection.query(query_texts=[query], n_results=1)
    return docs["documents"][0] if docs["documents"] else "No relevant information found."


add_doc_tool = Tool(
    name="AddDocument",
    func=add_document,
    description="Adds a document containing app-related information."   
)

search_doc_tool = Tool(
    name="SearchDocument",
    func=search_document,
    description="Searches for relevant information in stored documents."
)