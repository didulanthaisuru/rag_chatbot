from langchain_google_genai import GoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from config import GEMINI_API_KEY
from tools import transaction_tool
from todo import add_task_tool, get_tasks_tool
from rag import add_doc_tool, search_doc_tool

# Initialize Gemini Flash LLM
llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GEMINI_API_KEY)

# List of tools
tools = [transaction_tool, add_task_tool, get_tasks_tool, add_doc_tool, search_doc_tool]

# Define system message
system_prompt = """
You are a financial assistant that helps users with transactions, to-do lists, and app-related questions.
DO NOT answer unrelated questions like elections or politics.
If asked about unrelated topics, respond with: 'I can only assist with financial and app-related queries.'
"""

# Create the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    system_message=system_prompt,
    verbose=True
)

# Test queries
if __name__ == "__main__":
    print(agent.run("Paid $300 for electronics at Best Buy on 2025-02-20"))
    print(agent.run("Add 'Complete AI project' to my to-do list"))
    print(agent.run("Show my to-do list"))
    print(agent.run("What is the latest election update in Sri Lanka?"))
    print(agent.run("Add 'This app helps track transactions and expenses' to the knowledge base"))
    print(agent.run("Tell me about this app"))
