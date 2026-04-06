import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
if api_key is None:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")
    
print(f"GEMINI_API_KEY: {api_key}")


client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.5-flash", contents ="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")

print(response.text)