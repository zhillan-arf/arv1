from fetchers.oai import oai_infer
import json

filename = "backend/templates/request.json"

with open(filename, "r") as fp:
    chats = json.load(fp)

response = oai_infer(chats)

print(response.output_text)
print(response.output[0].content[0].text)
print(response.output[0].role)