from google.adk.agents import Agent


# Define the agent
# Define the agent
root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.5-flash",
    description="Greeting agent",
    instruction="""
    You are a helpful assistant that greets the user warmly.
    Ask the user for their name and respond with a personalized greeting.
    """
)
