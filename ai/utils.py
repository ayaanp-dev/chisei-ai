from dotenv import load_dotenv
import os
from groq import Groq

# Load environment variables
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not set in environment variables")

client = Groq(api_key=groq_api_key)

def create_chat_completion(messages: list, model: str):
    """Helper function to create chat completions."""
    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error generating response: {e}"