from openai import OpenAI
from config import load_api_key
client = OpenAI(api_key=load_api_key())

response = client.responses.create(
    model="gpt-5-nano",
    input="Make a sea shanty"
)

print(response.output_text)