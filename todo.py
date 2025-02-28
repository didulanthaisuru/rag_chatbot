from langchain.tools import Tool

todo_list = []

def add_task(task):
    todo_list.append(task)
    return f"Task '{task}' added to your to-do list."

def get_tasks(_):
    if not todo_list:
        return "Your to-do list is empty."
    return "\n".join([f" - {task}" for task in todo_list])

add_task_tool = Tool(
    name="GetToDo",
    fanc=add_task,
    description="Adds a task to the to-do list."
)

get_tasks_tool=Tool(
    name="GetToDo",
    func=get_tasks,
    description="Gets all tasks from the to-do list."
)