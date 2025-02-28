from langchain_google_genai import GoogleGenerativeAI
from config import GEMINI_API_KEY
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize Gemini in LangChain
llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GEMINI_API_KEY)

# Define a prompt template
prompt_template = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in 2 sentences."
)

# Create an LLM chain
chain = LLMChain(llm=llm, prompt=prompt_template)

# Test Prompt
response = chain.run("LangChain")
print(response)
