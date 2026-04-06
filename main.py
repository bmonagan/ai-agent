import os
import argparse
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
if api_key is None:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

    
client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("_user_prompt", type=str, help="User prompt")
args = parser.parse_args()
content = args._user_prompt
response = client.models.generate_content(
    model="gemini-2.5-flash", contents=content)

if not response.usage_metadata:
    print("No usage metadata found in the response.")
else:
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
print("Response:")
print(response.text)