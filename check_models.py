from google import genai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file in the 1-basic-agent folder
load_dotenv("1-basic-agent/greeting_agent/.env")
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("Error: GOOGLE_API_KEY not found. Check your .env file path.")
else:
    client = genai.Client(api_key=api_key)

    print("--- Available Models ---")
    try:
        for m in client.models.list():
            # Simply print the name and supported methods to see the structure
            print(f"Name: {m.name}")
            # print(f"Methods: {m.supported_methods}\n")
    except Exception as e:
        print(f"An error occurred: {e}")