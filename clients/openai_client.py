import asyncio
import os

from langchain_openai import ChatOpenAI

from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp import ClientSession


llm = ChatOpenAI(
    model=os.getenv('OPEN_AI_MODEL'),
    temperature=0.3,
    openai_api_key=os.getenv("OPEN_API_KEY"),
    openai_api_base=os.getenv('API_BASE_URL'))

async def main():
    server = StdioServerParameters(command="python",args=["server.py"])
    async with stdio_client(server) as (r, w):
        async with ClientSession(r, w) as session:

            # Initialize MCP session
            await session.initialize()

            # Get MCP tools
            mcp_tools = await session.list_tools()

            print("Available MCP tools:")
            for tool in mcp_tools.tools:
                print(f"- {tool.name}: {tool.description}")

            # Convert MCP tools to LangChain tools
            tools = []
            for t in mcp_tools.tools:
                tool = {
                    "name": t.name,
                    "description": t.description or "MCP tool",
                    "input_schema": t.inputSchema
                }
                tools.append(tool)

            # Bind tools to ChatOpenAI
            llm_with_tools = llm.bind_tools(tools)

            # User question
            response = await llm_with_tools.ainvoke(
                "Insert task Learn MCP OpenAIII"
            )

            # Check whether model requested an MCP tool
            if response.tool_calls:
                tool_call = response.tool_calls[0]
                tool_name = tool_call["name"]
                tool_arguments = tool_call["args"]
                print("Executing MCP tool:",tool_name)
                print("Arguments:",tool_arguments)              


                # Execute MCP tool
                result = await session.call_tool(tool_name,tool_arguments)
                print("MCP result:", result)
            else:
                print("Model response:",response.content)