from langchain_community.vectorstores import Chroma  # Fixed import
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # Fixed import
from langchain.tools import Tool
from langchain.docstore.document import Document
from config import GEMINI_API_KEY

# Initialize embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GEMINI_API_KEY)

# Initialize ChromaDB
chroma_client = Chroma(persist_directory="db/", embedding_function=embeddings)

# Function to add documents to the vector store
def add_document(text: str) -> str:
    doc = [Document(page_content=text)]
    chroma_client.add_documents(doc)
    return "Document added successfully."

# Function to search documents
def search_document(query: str) -> str:
    results = chroma_client.similarity_search(query, k=1)
    return results[0].page_content if results else "No relevant information found."

# Define tools
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
