import sys
import os
from google import genai
from dotenv import load_dotenv


def main():
    load_dotenv()

    args = sys.argv[1:] # gather the words from the input, ignore the script name

    if not args: # if no input was passed
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do i build a calulater app?"')
        sys.exit(1)
    user_prompt = " ".join(args) # joins args into a string with spaces

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=user_prompt
    )
    if len(sys.argv) <= 1: # no arguments provided
        print("Error: No arguments provided.")
        sys.exit(1)
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
