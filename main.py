import os
import sys
import argparse
from google import genai
from dotenv import load_dotenv
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
 
client = genai.Client(api_key=api_key)

#argument parser implementation
parser =argparse.ArgumentParser(description="A simple argument parser")
parser.add_argument("--verbose", action="store_true")
parser.add_argument("prompt")
args = parser.parse_args()
#store conversation
messages = [
    types.Content(role="user", parts=[types.Part(text=args.prompt)]),
]
#generate the agent response
response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages
)
#check for -v flag, else just print response
if args.verbose:
    print(response.text)
    print(f"User prompt: {args.prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
if args.prompt:
    print(response.text)


