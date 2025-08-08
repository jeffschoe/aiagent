import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv

from prompts import system_prompt
from call_function import available_functions
from functions.call_function import call_function


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]: # [1:] to start at index 1, ignoring script name
        if not arg.startswith("--"): # ignores flags
            args.append(arg)
                              
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
            ),
    )
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    
    
    #print("Response:")
    #print(response.text) 

    if not response.function_calls:   
        return response.text
    
    for function_call_part in response.function_calls:
        #if verbose:
        #    print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        #else:
        #    print(f" - Calling function: {function_call_part.name}")
        
        function_call_result = call_function(function_call_part, verbose)
        if not function_call_result.parts[0].function_response.response:
            raise Exception("Fatal Exception occured.")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

if __name__ == "__main__":
    main()
