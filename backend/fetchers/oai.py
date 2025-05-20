from openai import OpenAI
from dotenv import load_dotenv
from os import getenv
load_dotenv()
client = OpenAI(api_key=getenv("OAI_KEY"))
MAX_TOKENS = 1000

def oai_infer(msgs, store=False):   
    # msgs: str | list of {role: str, content: str | list}
    # No instructions. Put instructions as the first msg

    response = client.responses.create(
        model = "gpt-4o-mini",
        input = msgs,
        store = store,
        max_output_tokens = MAX_TOKENS,
    )

    return response
