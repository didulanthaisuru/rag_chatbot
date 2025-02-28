from langchain.tools import Tool

# In-memory storage for tasks
tasks = []

# Function to add a task
def add_task(task: str) -> str:
    tasks.append(task)
    return f"Task '{task}' added successfully."

# Function to get tasks
def get_tasks() -> str:
    return "\n".join(tasks) if tasks else "No tasks found."

# Define tools
add_task_tool = Tool(
    name="AddTask",
    func=add_task,
    description="Adds a task to the to-do list."
)

get_tasks_tool = Tool(
    name="GetTasks",
    func=get_tasks,
    description="Retrieves the list of to-do tasks."
)
