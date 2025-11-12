from config import load_api_key
from openai import OpenAI

client = OpenAI(api_key=load_api_key())


# Content Generation
def generate():
    response = client.responses.create(model="gpt-5-nano", instructions="example", input="example")
    return response.output_text


def print_response():
    print(generate())


def main():
    print_response()


if __name__ == "__main__":
    main()
