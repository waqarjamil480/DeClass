import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import os

def load_to_google_sheet(**kwargs):
    # our csv file path
    csv = "/opt/airflow/dags/etl/data/consumer_complaints_transformed.csv"

    # checking if available
    if not os.path.exists(csv):
        print("CSV file not found!")
        return

    #  reading data from our transformed data csv
    df = pd.read_csv(csv)
    print(f"CSV loaded successfully, {len(df)} rows")



    # here authentication with downloaded json file from Gogle Service Account credentials
    creds_path = os.path.join(os.path.dirname(__file__), "consumer-complaints-etl.json")
    # auth for the service we will use like spreedsheets
    creds = Credentials.from_service_account_file(
        creds_path,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )


    # build service
    service = build("sheets", "v4", credentials=creds)
    SHEET_ID = "1hZY6iIMsSsx2PxhUCugI8oogPXqQAA485K-GEmDrZ34"   
    RANGE_NAME = "Sheet1!A1"   # go to sheet 1 and select cell A1
    data = [df.columns.tolist()] + df.values.tolist()

    # Clear sheet data
    service.spreadsheets().values().clear(
        spreadsheetId=SHEET_ID,
        range=RANGE_NAME
    ).execute()



    # upload new data
    service.spreadsheets().values().update(
        spreadsheetId=SHEET_ID,
        range=RANGE_NAME,
        valueInputOption="RAW",
        body={"values": data}
    ).execute()



    print("All data has been uploaded to googlesheet")
