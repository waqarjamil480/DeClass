import pandas as pd 
from airflow.providers.mysql.hooks.mysql import MySqlHook

def transform_data(**kwargs):
    mysql_hook = MySqlHook(mysql_conn_id='mysql_complaints')

    # selecting all data from table
    sql = "SELECT * FROM consumer_complaints"
    # fetching all data in pandas dataframes
    df = mysql_hook.get_pandas_df(sql)
    #size of the DataFrame in terms of rows and columns.
    print("fetching all data from mysql:", df.shape)

    # droping columns from required tranformation 
    drop_col = [
        "complaint_what_happened",
        "date_sent_to_company",
        "zip_code",
        "tags",
        "has_narrative",
        "consumer_consent_provided",
        "consumer_disputed",
        "company_public_response"
    ]
    df = df.drop(columns=drop_col, errors="ignore")
    print("transformed count after droping columns:", df.shape)

    # converting  col date_received data  in  month-year 
    # If invalid date exists --> convert to NaT instead of crashing.

    df["month_year"] = pd.to_datetime(df["date_received"], errors="coerce").dt.strftime("%m-%y")
    print("created month_year col")

    # grouping as per shared csv in transformation example
    group_cols = [
        "product",
        "sub_product",
        "issue",
        "sub_issue",
        "submitted_via",
        "company",
        "state",
        "timely",
        "company_response",
        "month_year"
    ]
    # replacing all NaN (missing values) in group_cols(list of above cols) with "Not Available". 
    df[group_cols] = df[group_cols].fillna("Not Available")

    # now distinct count by using above col complaint_id as per transformation required 
    #Do NOT ignore missing values (NaN) dropna=False
    #complaint_count=("complaint_id", "nunique")     new required col and taking unique values like 3,3   unique value is 3 and count is 1 not 2 
    transform_df = df.groupby(group_cols, dropna=False).agg(
        count_of_complaint_id=("complaint_id", "nunique")
    ).reset_index()
    #reset_index() converts them back to normal columns
    print("transformation is complete", transform_df.shape)

    # saving transformed data into csv    
    transform_df.to_csv('/opt/airflow/dags/etl/data/consumer_complaints_transformed.csv', index=False)
    print("saved successfully")

    return "CSV saved."