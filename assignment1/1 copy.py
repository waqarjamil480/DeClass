from dotenv import load_dotenv
import os,requests,json
load_dotenv("assignment1/.env", override=True)
llm_api_key = os.getenv("llm_token")


headers_llm = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {llm_api_key}',
}

json_data_llm = {
    'model': 'Meta-Llama-3.1-8B-Instruct',   # ✅ correct model name for SambaNova
    'messages': [
        {
            'role': 'system',
            'content': 'Converts the given text news into humorous content with emojis.',
        },
        {
            'role': 'user',
            'content': 'Convert this news into humorous version with emojis: Get the latest national, international, and political news at USATODAY.com.',
        },
    ],
    'max_tokens': 200,
    'temperature': 0.8,
}

try:

    llm_response = requests.post(
        'https://api.cloud.sambanova.ai/v1/chat/completions',
        headers=headers_llm,
        json=json_data_llm
    )

    # check status first
    if llm_response.status_code == 200:

        llm_result = llm_response.json()

        humorous_text = llm_result['choices'][0]['message']['content']

        print("\nHumorous Text:\n")
        print(humorous_text)

    else:
        print("Error Status:", llm_response.status_code)
        print("Error Message:", llm_response.text)

except requests.exceptions.RequestException as e:
    print("Request Failed:", e)