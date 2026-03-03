from airflow.sdk import DAG
from datetime import datetime, timedelta
# from airflow.operators.python import PythonOperator
# from airflow.sensors.filesystem import FileSensor
# from airflow.operators.email import EmailOperator   old outdated 
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.sensors.filesystem import FileSensor
from airflow.providers.smtp.operators.smtp import EmailOperator
#---IMPORTING ALL FUNCTIONS FROM EXTERNAL FILES---#
from etl.extract import extract as extract_data
from etl.load import dump_to_mysql
from etl.transform import transform_data
from etl.load_google_sheet import load_to_google_sheet
#---IMPORTING ALL FUNCTIONS FROM EXTERNAL FILES---#
default_args = {
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=3),
    # "execution_timeout": timedelta(seconds=300),
    "email_on_failure": True,
    "email": ["waqarjamil480@gmail.com"],  
}

with DAG(
    dag_id = 'consumer_financial_etl',
    default_args=default_args,
    description="Airflow Orchestration for Consumer Financial Complaints",
    schedule="0 0 * * *",   # runs daily at 12 AM midnight / Run at 00:00 (12:00 AM) every day
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["Consumer_complaints", "ETL", "kai_batch10"]
) as dag:
    # extract_task = task(
    #     task_id="extract_data_from_source"
    # )(extract_run)     // more better way to use 

    extract_task = PythonOperator(
        task_id = 'extract_data_from_source',
        python_callable=extract_data
    )
    dump_mysql_task = PythonOperator(  # this will load.py
        task_id = 'dump_data_to_mysql',
        python_callable=dump_to_mysql    
    )

    transform_task = PythonOperator(
        task_id = 'transform_data',
        python_callable=transform_data
    )

    check_file_task  = FileSensor(
        task_id="check_consumer_financial_csv",
        filepath="/opt/airflow/dags/etl/data/consumer_complaints_transformed.csv",  
        poke_interval=10,  #airflow will check file after every 10secs if not exists 
        timeout=300,     #max time wait is 5mins if not found then fail this task
        mode='poke',        # or 'reschedule' to free the worker here --> Worker occupied --> checking --> checking --> checking
        #fs_conn_id='fs_default',  # this is the connection --> Where to look for file -->/opt/airflow/and file
    )

    load_task = PythonOperator(    # this will load_google_sheet.py
        task_id = 'dump_googlesheet',
        python_callable=load_to_google_sheet
    )

    send_email_task = EmailOperator(
        task_id = 'send_googlesheet_url_via_email',
        to=["waqarjamil488@gmail.com", "waqarjamil481@gmail.com"],
        subject="Google Sheet File url - Consumer Complaints",
        html_content="""
                        <b>Hello Dear,</b>
                        <p>The Consumer Complaints Transformed data - Google Sheet.</p>
                        <p>
                        Please check Google Sheet File url - Consumer Complaints:
                        <a href="https://docs.google.com/spreadsheets/d/1hZY6iIMsSsx2PxhUCugI8oogPXqQAA485K-GEmDrZ34/edit?usp=sharing">
                        Google Sheet
                        </a>
                        </p>
                    """,
        conn_id="smtp_default"    
    )

    extract_task >> dump_mysql_task >> transform_task >> check_file_task >> load_task >> send_email_task