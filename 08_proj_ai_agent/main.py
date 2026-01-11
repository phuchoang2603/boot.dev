import argparse
from inspect import _empty
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import SYSTEM_PROMPT
from functions.call_functions import available_functions, call_function


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("api key not found")

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=SYSTEM_PROMPT, temperature=0
        ),
    )

    if response.usage_metadata is None:
        raise RuntimeError("usage metadata is None")

    if args.verbose is True:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    function_results = []

    if response.function_calls is not None:
        for function_call in response.function_calls:
            function_call_result = call_function(function_call, verbose=args.verbose)

            if function_call_result.parts is None:
                raise Exception("Error: Empty parts list")
            if function_call_result.parts[0].function_response is None:
                raise Exception("Error: Incorrect type returned")

            function_response = function_call_result.parts[0].function_response.response
            if function_response is None:
                raise Exception("Error: Empty response")
            if args.verbose is True:
                print(f"-> {function_response}")

            function_results.append(function_call_result.parts[0])
    else:
        print(response.text)


if __name__ == "__main__":
    main()
