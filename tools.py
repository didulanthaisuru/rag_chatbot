from langchain.tools import Tool
from transaction import process_transaction

# Tool for handling transactions
transaction_tool = Tool(
    name="TransactionProcessor",
    func=process_transaction,
    description="Processes user transactions and stores details."
)
