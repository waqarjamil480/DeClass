import time
from dotenv import load_dotenv
import os, requests, json

# Load API key
load_dotenv("assignment1/.env", override=True)
groq_api_key = os.getenv("llm_token2")

# Headers


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {groq_api_key}",
}

json_data_llm = {
    "model": "llama-3.1-8b-instant",  # or another available Groq model
    "messages": [
        {
            "role": "system",
            "content": "Convert news into humorous content with emojis in max 1 line max 400 char."
        },
        {
            "role": "user",
            "content": f"Convert this news into humorous version with emojis: the world will be finshed on 2028."
        }
    ],
    "max_tokens": 150,   # Increase this
    "temperature": 0.7
}

response = requests.post(
    "https://api.groq.com/openai/v1/chat/completions",
    headers=headers,
    json=json_data_llm
)

result = response.json()
print(result["choices"][0]["message"]["content"])


# print(json.dumps(result, indent=4, ensure_ascii=False))

