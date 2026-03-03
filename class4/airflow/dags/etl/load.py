import os
import pandas as pd
from airflow import DAG
from airflow.providers.mysql.hooks.mysql import MySqlHook
from datetime import datetime, timedelta


def dump_to_mysql(**kwargs):
    mysql_conn_id = "mysql_complaints"
    # xcom se path get 
    ti = kwargs['ti']    #'took task instance key ti from xcom'
    file_path = ti.xcom_pull(task_ids='extract_data_from_source') 

    if not file_path:
        print("no file path")
        return

    print("load data from:", file_path)

    # read csv file 
    df = pd.read_csv(file_path)
    print("sucessuffly read", len(df))

    # if nan then replace to none  blank with null
    df = df.replace({pd.NA: None})
    df = df.replace({float("nan"): None})

    # sql
    mysql_hook = MySqlHook(mysql_conn_id=mysql_conn_id)


    # Create table
    mysql_hook.run("""
    CREATE TABLE IF NOT EXISTS consumer_complaints (
        id INT AUTO_INCREMENT PRIMARY KEY,
        product VARCHAR(255),
        complaint_what_happened TEXT,
        date_sent_to_company VARCHAR(40),
        issue TEXT,
        sub_product VARCHAR(255),
        zip_code VARCHAR(10),         
        tags VARCHAR(50),
        has_narrative BOOLEAN,          
        complaint_id BIGINT,
        timely VARCHAR(10),
        consumer_consent_provided VARCHAR(100),       
        company_response VARCHAR(255),
        submitted_via VARCHAR(100),
        company VARCHAR(255),
        date_received VARCHAR(40),           
        state VARCHAR(10),
        consumer_disputed VARCHAR(15),
        company_public_response TEXT,
        sub_issue TEXT
    );
    """)

    # Insert rows
    mysql_hook.insert_rows(
        table="consumer_complaints",
        #This will converts the DataFrame into a NumPy array and then .tolist() Converts that array into a Python list of lists
        rows=df.values.tolist(),
        target_fields=list(df.columns),
    )





    # Insert rows
    #  for _, row in df.iterrows():
    #     mysql_hook.run(
    #         sql="""
    #         INSERT INTO consumer_complaints 
    #         (product, complaint_what_happened, date_sent_to_company, issue, sub_product, zip_code, tags, has_narrative, complaint_id, timely, consumer_consent_provided, company_response, submitted_via, company, date_received, state, consumer_disputed, company_public_response, sub_issue)
    #         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    #         """,
    #         parameters=[
    #             row['product'], 
    #             row['complaint_what_happened'], 
    #             row['date_sent_to_company'], 
    #             row['issue'], 
    #             row['sub_product'], 
    #             row['zip_code'], 
    #             row['tags'], 
    #             row['has_narrative'], 
    #             row['complaint_id'], 
    #             row['timely'], 
    #             row['consumer_consent_provided'], 
    #             row['company_response'], 
    #             row['submitted_via'], 
    #             row['company'], 
    #             row['date_received'], 
    #             row['state'], 
    #             row['consumer_disputed'], 
    #             row['company_public_response'], 
    #             row['sub_issue'], 
    #         ],
    #         autocommit=True
    #     )