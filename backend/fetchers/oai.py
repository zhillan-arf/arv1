from openai import OpenAI
from dotenv import load_dotenv
from os import getenv
from classes import OAIMsg

MAX_TOKENS = 1000

load_dotenv()

client = OpenAI(
    api_key=getenv("OAI_KEY")
)

def OAIComplete(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens = MAX_TOKENS
    )

    return response.choices[0].message.content