from airflow.sdk import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from datetime import datetime, timedelta

with DAG(
    dag_id = 'consumer_financial_etl',
    description="Airflow Orchestration for Consumer Financial Complaints",
    schedule=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["kai", "batch10"]
) as dag:
    
    extract_task = EmptyOperator(
        task_id = 'extract_data_from_source'
    )

    dump_mysql_task = EmptyOperator(
        task_id = 'dump_data_to_mysql'
    )

    transform_task = EmptyOperator(
        task_id = 'transform_data'
    )

    check_file_task = EmptyOperator(
        task_id = 'check_consumer_financial_csv'
    )

    load_task = EmptyOperator(
        task_id = 'dump_googlesheet'
    )

    send_email_task = EmptyOperator(
        task_id = 'send_googlesheet_url_via_email'
    )

    extract_task >> dump_mysql_task >> transform_task >> check_file_task >> load_task >> send_email_task