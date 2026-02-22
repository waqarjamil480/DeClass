from flask import Flask,jsonify, request
from dotenv import load_dotenv
import os,requests,json, time

load_dotenv("assignment1/.env", override=True)
news_api_key = os.getenv("news_token")
llm_api_key = os.getenv("llm_token2")


app = Flask(__name__)

#sub function 1
##############fetch_news#########################
def fetch_news(params: dict):
    endpoint = "top-headlines"   #'everything','top-headlines' there are two endpoints available in newsapi.

    url = f"https://newsapi.org/v2/{endpoint}/sources"
    headers = {
        "X-Api-Key":news_api_key
    }
    response = requests.get(url, headers=headers, params=params)
    #response.url
    status_code = response.status_code

    if status_code == 200:

        all_news = response.json()
        number_of_sources = len(all_news['sources'])
        news_list = []
        if number_of_sources >= 1:
            print(f"\nTotal Results in country {params['country']}: {number_of_sources}\n")
            i = 1 
            for article in all_news['sources']:
                # print(f"Name: {article['name']}")
                # print(f"Description: {article['description']}")
                # print(f"URL: {article['url']}")
                # print(f"Country: {article['country']}")
                # print(f"Category: {article['category']}\n")

                # store in dictionary
                news_dict = {
                    "id":  i,
                    "title": article['name'],
                    "original_description": article['description'],
                    "url": article['url'],
                    "country": article['country'],
                    "category": article['category']
                }
                news_list.append(news_dict)

                i += 1
            return news_list
        else:
            print(f"No news articles found for the given query country:{params['country']} & category:{params['category']} or less than 0.")
    elif status_code == 400:
        print("Bad Request: The request was invalid. Please check your parameters.")
    elif status_code == 401:
        print("Unauthorized: Invalid API key. Please check your API key.")

##############fetch_news#########################







# country=ir&category=general&q=a
#country=  #us in ar de en es fr he it nl no pt ru sv ud zh
# category= business, entertainment, general, health, science, sports, technology
@app.route('/humor-news', methods=['GET'])
def humor_news():
    if not request.args:
        return jsonify({
            "error": "Missing query parameters",
            "message": "Please provide url query parameter details like ?country=in&category=business&q=a"
        }), 400   # 400 = Bad Request

    params={
        "q": request.args.get('q', 'AI'),
        'country': request.args.get('country', 'in'),   #us in ar de en es fr he it nl no pt ru sv ud zh
        "category": request.args.get('category', 'general'),   #business, entertainment, general, health, science, sports, technology
        "pageSize": 10,  # for pagination, number of results per page
        "page": 1  # we need only 1 page of results with 10 articles per page
    }
    #https://newsapi.org/v2/top-headlines/sources?apiKey=3b277188c75a4c4f88414305bdc7cb4e&country=us&category=business&pageSize=10&q=AI
    #https://newsapi.org/v2/top-headlines?country=us&apiKey=3b277188c75a4c4f88414305bdc7cb4e    
    #source endpoint is showing other countries headlines otherwise only showing US result on removing source endpoint.
        
    #pass params to another func 
    news_list = fetch_news(params)

    ##############humorous version#########################here
    def convert_to_humor(news_text):
        headers_llm = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {llm_api_key}', 
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
                    "content": f"Convert this news into humorous version with emojis: {news_text}"
                }
            ],
            "max_tokens": 500,   # Increase this
            "temperature": 0.7
        }



        # Retry logic (3 attempts)
        for attempt in range(3):

            llm_response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
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









    ##############Processing all_news_data  to  humorous version function#########################

    # Process all news
    print("Processing news...\n")

    for news in news_list:

        print(f"Processing News ID: {news['id']}")

        #called function to convert news --> convert_to_humor(that news string 0ne by one by loop)
        humorous_version = convert_to_humor(news["original_description"])

        # humorous_version = news["original_description"] + ' 😂 test humor'

        #we are Adding coverted news into same dictionary beacuse in loop   news(reference) == news_list
        news["humorous_news"] = humorous_version

        # Small delay to avoid rate limit
        time.sleep(2)


    # Final updated list
    print("\nFinal Updated News List:\n")

    print(json.dumps(news_list, indent=4, ensure_ascii=False))

     ##############Processing all_news_data  to  humorous version function#########################


    # create final structured dict
    final_response = {
        "status": "success",
        "length": len(news_list),
        "data": news_list
    }

    # Save to file
    with open("updated_news.json", "w", encoding="utf-8") as f:
        json.dump(final_response, f, indent=4, ensure_ascii=False)

    print("\nSaved to updated_news.json")
    # Save to file


    return jsonify({
        "message": "Saved to updated_news.json",
        "total_results": len(news_list),
        "data": news_list
    }), 200




if __name__ == '__main__':
    app.run(host='0.0.0.0', port ='5000', debug=True)