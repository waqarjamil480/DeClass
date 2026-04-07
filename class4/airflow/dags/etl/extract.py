import os, time
import requests
import pandas as pd
from datetime import date, timedelta
#for states 
# https://gist.githubusercontent.com/mshafrir/2646763/raw/8b0dbb93521f5d6889502305335104218454c2bf/states_hash.json

# for required data
# https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/?field=complaint_what_happened&size=500&date_received_max=2021-11-02&date_received_min=2020-11-02&state=WA


# url = "https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/"
# params = {
#     "field": "complaint_what_happened",
#     "size": 500,
#     "date_received_max": "2026-03-02",
#     "date_received_min": "2026-01-31",
#     "state": "AL"
# }
# response = requests.get(url, params=params)
# data = response.json()["hits"]["hits"]
# response.url

# print(len(data))  


def extract(**kwargs):
    api_url = 'https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/'
    size =   500 # Following fixed required data as per doc
    all_states = 'https://gist.githubusercontent.com/mshafrir/2646763/raw/8b0dbb93521f5d6889502305335104218454c2bf/states_hash.json'

    #  User-Agent so that it will not block us on many requests
    headers = {
        "User-Agent": (
            "Chrome/115.0 Safari/537.36"
            "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
        )
    }
    # Fetching all states 
    response_all_states = requests.get(all_states, headers=headers)
    response_all_states.raise_for_status() # if api failed so dont go / fail immediately
    all_states = response_all_states.json()
    # print(response_all_states.json())
    # print(f"Total states fetched: {len(all_states)}")
    # Fetching all states 


    # For a month
    today = date.today()
    # print(today)  y m d
    last_month = today - timedelta(days=30)
    # print(last_month) y m d
    raw_data_all = []
    # for every state
    for all_states_data in all_states.keys():   # getting only key name due to requirement like AL,AK... to pass loop wide for each api call for data
        #size=500&date_received_max={}&date_received_min={}&state={}
        
        params = {
            "field": "complaint_what_happened",
            "size": size,
            "date_received_max": today.isoformat(),
            "date_received_min": last_month.isoformat(),
            "state": all_states_data
        }
        #time.sleep(0.01) #10 milliseconds
        response = requests.get(api_url, params=params, headers=headers)
        data = response.json().get("hits", {}).get("hits", [])
        raw_data_all.extend(data)
        


    # for store data in csv file
    if raw_data_all:   #if it has data  
        data_file = pd.DataFrame([data_r["_source"] for data_r in raw_data_all])  
        file_path = os.path.expanduser("/opt/airflow/dags/etl/data/Raw_Consumer_Complaints.csv")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        data_file.to_csv(file_path, index=False)
        print(f"Total: {len(data_file)} Saved records")
        return file_path     # this will store the the file path in xom
        # ti.xcom_push(
        #     key="return_value",
        #     value=file_path
        # )
    else:
        print("No data fetched!")
        return None

if __name__ == "__main__":
    extract()
