from langchain_google_genai import GoogleGenerativeAI
from config import GEMINI_API_KEY

# Initialize Gemini Flash model
llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GEMINI_API_KEY)

# Test prompt
response = llm.invoke("What is LangChain?")
print(response)
