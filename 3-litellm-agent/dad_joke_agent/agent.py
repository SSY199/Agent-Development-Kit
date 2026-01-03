import os
import random

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
# OpenRouter model (FREE)
model = LiteLlm(
    model="openrouter/meta-llama/llama-3.1-8b-instruct",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


def get_random_dad_joke() -> dict:
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call cheese that isn't yours? Nacho cheese!",
    ]
    return {"joke": random.choice(jokes)}


root_agent = Agent(
    name="dad_joke_agent",
    model=model,
    description="An agent that tells dad jokes.",
    instruction="""
You are a dad joke agent.
When a user asks for a dad joke, call the get_random_dad_joke tool
and return the joke to the user.
""",
    tools=[get_random_dad_joke],
)
