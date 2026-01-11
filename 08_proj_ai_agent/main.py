import argparse
import os
from functools import reduce
from typing import List, Optional, Callable

from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import SYSTEM_PROMPT, MODEL
from functions.call_functions import available_functions, call_function


# ============================================================================
# Pure Functions (no side effects)
# ============================================================================


def get_api_key(env_var: str = "GEMINI_API_KEY") -> str:
    """Pure function to extract API key from environment"""
    api_key = os.environ.get(env_var)
    if api_key is None:
        raise RuntimeError("Error: api key not found")
    return api_key


def create_initial_message(user_prompt: str) -> types.Content:
    """Pure function to create initial user message"""
    return types.Content(role="user", parts=[types.Part(text=user_prompt)])


def extract_candidates(response) -> List[types.Content]:
    """Pure function to extract candidate contents from response"""
    if response.candidates is None:
        return []

    contents = []
    for candidate in response.candidates:
        if candidate.content is None:
            raise RuntimeError("Error: Empty content")
        contents.append(candidate.content)
    return contents


def has_function_calls(response) -> bool:
    """Pure function to check if response has function calls"""
    return response.function_calls is not None


def extract_function_calls(response):
    """Pure function to extract function calls from response"""
    return response.function_calls if response.function_calls is not None else []


def get_response_text(response) -> Optional[str]:
    """Pure function to safely extract response text"""
    return response.text if hasattr(response, "text") else None


# ============================================================================
# Higher-Order Functions & Function Composition
# ============================================================================


def create_verbose_logger(enabled: bool) -> Callable:
    """Higher-order function that returns a logger based on verbosity"""

    def log(message: str) -> None:
        if enabled:
            print(message)

    return log


def compose(*functions):
    """Function composition: compose(f, g, h)(x) = f(g(h(x)))"""
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


def process_function_call(verbose: bool):
    """Returns a function that processes a single function call"""
    log = create_verbose_logger(verbose)

    def processor(function_call):
        function_call_result = call_function(function_call, verbose=verbose)

        # Validation chain
        if function_call_result.parts is None:
            raise Exception("Error: Empty parts list")
        if function_call_result.parts[0].function_response is None:
            raise Exception("Error: Incorrect type returned")

        function_response = function_call_result.parts[0].function_response.response
        if function_response is None:
            raise Exception("Error: Empty response")

        log(f"-> {function_response}")
        return function_call_result.parts[0]

    return processor


def process_function_calls(function_calls, verbose: bool) -> List:
    """
    Functional approach to processing function calls using map.
    This replaces the imperative for loop with a declarative map.
    """
    processor = process_function_call(verbose)
    return list(map(processor, function_calls))


# ============================================================================
# Core Generation Logic
# ============================================================================


def create_generator(client):
    """Higher-order function that creates a content generator with config"""

    def generate(messages):
        return client.models.generate_content(
            model=MODEL,
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=SYSTEM_PROMPT,
                temperature=0,
            ),
        )

    return generate


def log_usage_metadata(response, user_prompt: str, verbose: bool) -> None:
    """Side effect: Log usage metadata if verbose"""
    if not verbose:
        return

    if response.usage_metadata is None:
        raise RuntimeError("Error: usage metadata is None")

    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


def conversation_step(generate, messages: List, user_prompt: str, verbose: bool):
    """
    Pure logic for a single conversation step.
    Returns: (should_continue, new_messages)
    """
    response = generate(messages)

    # Append candidates to messages
    candidates = extract_candidates(response)
    new_messages = messages + candidates

    # Log metadata (side effect)
    log_usage_metadata(response, user_prompt, verbose)

    # Check if we have function calls or final text
    if has_function_calls(response):
        # Process function calls functionally
        function_parts = process_function_calls(
            extract_function_calls(response), verbose
        )
        # Append function responses
        function_message = types.Content(role="user", parts=function_parts)
        return True, new_messages + [function_message]
    else:
        # Final response - print and stop
        text = get_response_text(response)
        if text:
            print(text)
        return False, new_messages


def conversation_loop(
    generate,
    initial_messages: List,
    user_prompt: str,
    verbose: bool,
    max_iterations: int = 20,
) -> bool:
    """
    Functional conversation loop using recursion-like iteration.
    Returns: True if conversation completed successfully, False if max iterations reached
    """
    messages = initial_messages

    for _ in range(max_iterations):
        should_continue, messages = conversation_step(
            generate, messages, user_prompt, verbose
        )
        if not should_continue:
            return True

    # Max iterations reached without final response
    return False


# ============================================================================
# Main Entry Point
# ============================================================================


def parse_arguments():
    """Pure function to parse command-line arguments"""
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    return parser.parse_args()


def main():
    # Side effects grouped at the beginning
    load_dotenv()
    args = parse_arguments()

    # Pure function pipeline
    api_key = get_api_key()
    client = genai.Client(api_key=api_key)
    generate = create_generator(client)
    initial_message = create_initial_message(args.user_prompt)

    # Run conversation loop
    success = conversation_loop(
        generate=generate,
        initial_messages=[initial_message],
        user_prompt=args.user_prompt,
        verbose=args.verbose,
        max_iterations=20,
    )

    # Handle max iterations reached
    if not success:
        print(
            "Error: Maximum iterations reached without final response from the model."
        )
        print(
            "The model kept requesting function calls but never provided a final answer."
        )
        exit(1)


if __name__ == "__main__":
    main()
