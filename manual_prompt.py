import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure Gemini Flash
genai.configure(api_key=GEMINI_API_KEY)

# Function to call Gemini manually
def ask_gemini(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

# Test Prompt
response = ask_gemini("Explain LangChain in 2 sentences.")
print(response)
