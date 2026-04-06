import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
if api_key is None:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")
print(f"GEMINI_API_KEY: {api_key}")