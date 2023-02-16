import argparse
import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_TOKEN")


def generate_improved_text(text):
    # Define the prompt
    prompt = f"Please check the spelling and grammar, and improve the expression and legibility of the following text:\n{text}"

    # Generate the improved text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Return the generated text
    return response.choices[0].text


if __name__ == "__main__":
    # Define and parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to the input text file")
    args = parser.parse_args()

    # Load the input text
    with open(args.input_file, "r") as f:
        input_text = f.read()

    # Generate the improved text
    improved_text = generate_improved_text(input_text)

    # Print the generated text
    print(improved_text)
