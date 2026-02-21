import time
from dotenv import load_dotenv
import os, requests, json

# Load API key
load_dotenv("assignment1/.env", override=True)
llm_api_key = os.getenv("llm_token")

# Headers
headers_llm = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {llm_api_key}',
}

# Your news list (input)
news_list = [
    {"id": 1, "news": "Global markets rise amid economic optimism."},
    {"id": 2, "news": "Fuel prices expected to increase next month."},
    {"id": 3, "news": "New smartphone model released worldwide."},
    {"id": 4, "news": "Heavy rains cause flooding in several cities."},
    {"id": 5, "news": "Scientists discover new species in Amazon."},
    {"id": 6, "news": "Political leaders meet for climate discussion."},
    {"id": 7, "news": "Space mission reaches Mars orbit."},
    {"id": 8, "news": "New education reforms announced."},
    {"id": 9, "news": "Tech companies announce layoffs."},
    {"id": 10, "news": "Sports team wins championship."}
]


# Function to convert news into humorous version
def convert_to_humor(news_text):

    json_data_llm = {
        'model': 'Meta-Llama-3.1-8B-Instruct',
        'messages': [
            {
                'role': 'system',
                'content': 'Convert news into humorous content with emojis in max 1 line max 400 char.'
            },
            {
                'role': 'user',
                'content': f'Convert this news into humorous version with emojis: {news_text}'
            }
        ],
        'max_tokens': 60,
        'temperature': 0.7,
    }

    # Retry logic (3 attempts)
    for attempt in range(3):

        llm_response = requests.post(
            'https://api.sambanova.ai/v1/chat/completions',
            headers=headers_llm,
            json=json_data_llm
        )

        if llm_response.status_code == 200:

            llm_result = llm_response.json()

            humorous_text = llm_result["choices"][0]["message"]["content"]

            return humorous_text


        elif llm_response.status_code == 429:

            print(f"Rate limit hit for news. Attempt {attempt+1}/3. Waiting 20 seconds...")
            time.sleep(20)


        else:

            print("Error:", llm_response.json())
            return None


# Process all news
print("Processing news...\n")

for news in news_list:

    print(f"Processing News ID: {news['id']}")

    #called function to convert news --> convert_to_humor(that news string 0ne by one by loop)
    humorous_version = convert_to_humor(news["news"])

    #we are Adding coverted news into same dictionary beacuse in loop   news(reference) == news_list
    news["humorous_news"] = humorous_version

    # Small delay to avoid rate limit
    time.sleep(4)


# Final updated list
print("\nFinal Updated News List:\n")

print(json.dumps(news_list, indent=4, ensure_ascii=False))


# Optional: Save to file
# with open("updated_news.json", "w", encoding="utf-8") as f:

#     json.dump(news_list, f, indent=4, ensure_ascii=False)

# print("\nSaved to updated_news.json")









##############humorous version#########################
def convert_to_humor(news_text):
    headers_llm = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {llm_api_key}',
    }
    json_data_llm = {
        'model': 'Meta-Llama-3.1-8B-Instruct',
        'messages': [
            {
                'role': 'system',
                'content': 'Convert news into humorous content with emojis in max 1 line max 400 char.'
            },
            {
                'role': 'user',
                'content': f'Convert this news into humorous version with emojis: {news_text}'
            }
        ],
        'max_tokens': 60,
        'temperature': 0.7,
    }

    # Retry logic (3 attempts)
    for attempt in range(3):

        llm_response = requests.post(
            'https://api.sambanova.ai/v1/chat/completions',
            headers=headers_llm,
            json=json_data_llm
        )

        if llm_response.status_code == 200:

            llm_result = llm_response.json()

            humorous_text = llm_result["choices"][0]["message"]["content"]

            return humorous_text


        elif llm_response.status_code == 429:

            print(f"Rate limit hit for news. Attempt {attempt+1}/3. Waiting 20 seconds...")
            time.sleep(20)


        else:

            print("Error:", llm_response.json())
            return None

##############humorous version#########################