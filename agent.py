from langchain_google_genai import GoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from config import GEMINI_API_KEY
from tools import transaction_tool

# Initialize Gemini Flash
llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GEMINI_API_KEY)

# List of tools
tools = [transaction_tool]

# Create the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True  # Shows logs for debugging
)

# Test the agent
query = "Paid $200 for groceries at Walmart on 2025-02-12"
response = agent.run(f"Summarize this transaction: {query}")
print(response)
