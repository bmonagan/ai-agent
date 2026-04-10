import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt, model_name
load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')
if api_key is None:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

# Initialize the GenAI client with the API key
client = genai.Client(api_key=api_key)

# Set up argument parsing to get the user prompt from the command line
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
content = args.user_prompt
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

# Generate content using the specified model and the user prompt
response = client.models.generate_content(
    model=model_name,
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
)

# Check if usage metadata is available in the response and print token counts
if not response.usage_metadata:
    print("No usage metadata found in the response.")
else:
    if args.verbose:
        print(f"User prompt: {content}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:")
    print(response.text)
