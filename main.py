import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt, model_name
from functions.call_function import available_functions, call_function
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
    config=types.GenerateContentConfig
    (tools = [available_functions],
    system_instruction=system_prompt),
)

# Check if usage metadata is available in the response and print token counts
if not response.usage_metadata:
    print("No usage metadata found in the response.")
else:
    if args.verbose:
        print(f"User prompt: {content}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    if response.function_calls and len(response.function_calls) > 0:
        function_call_result = call_function(response.function_calls[0], verbose=args.verbose)
        if not function_call_result.parts or not function_call_result.parts[0].function_response:
            raise Exception("No function response found in the function call result.")
        function_response = function_call_result.parts[0].function_response.response
        if function_response == None:
            raise Exception("Function response is None.")
        function_results = [function_call_result.parts[0]]
        if args.verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

    else:
        print(response.text)
