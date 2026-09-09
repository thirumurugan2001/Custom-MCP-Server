from mcp.server.fastmcp import FastMCP
from tools.read_tasks import read_tasks
from tools.insert_task import insert_task
from tools.delete_task import delete_task
from tools.update_task import update_task
from tools.read_table_schema import get_task_table_schema

mcp = FastMCP("mysql-tools")

@mcp.tool()
def read_tasks_tool():
    return read_tasks()

@mcp.tool()
def read_table_schema():
    return get_task_table_schema()

@mcp.tool()
def insert_task_tool(title: str):
    return insert_task(title)

@mcp.tool()
def delete_task_tool(task_id: int):
    return delete_task(task_id)

@mcp.tool()
def update_task_tool(task_id: int, title: str):
    return update_task(task_id, title)

if __name__ == "__main__":
    mcp.run()
    print("MCP SERVER STARTED")
    
