from langchain.tools import Tool
import re

# Function to extract transaction details
def transaction_summary(text):
    pattern = r"Paid \$(\d+) for (.+) at (.+) on (\d{4}-\d{2}-\d{2})"
    match = re.search(pattern, text)
    
    if match:
        amount, category, merchant, date = match.groups()
        return {
            "date": date,
            "amount": float(amount),
            "category": category,
            "merchant": merchant
        }
    return "Invalid transaction format"

# Wrap function as a LangChain tool
transaction_tool = Tool(
    name="TransactionSummary",
    func=transaction_summary,
    description="Extracts transaction details from a sentence."
)
