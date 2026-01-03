from datetime import datetime
from google.adk.agents import Agent
from google.adk.tools.google_search_tool import GoogleSearchTool


def get_current_time() -> dict:
    """Get the current time in the format YYYY-MM-DD HH:MM:SS."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": current_time}
  

root_agent = Agent(
  name="tool_agent",
    model="gemini-2.5-flash",
    description="Tool-enabled agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    # - google_search_tool: Use this tool to search the web for up-to-date information.
    - get_current_time: Use this tool to get the current time.
    """,
    tools=[get_current_time],
)