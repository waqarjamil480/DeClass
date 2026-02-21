from airflow.sdk import dag, task
from airflow.providers.smtp.operators.smtp import EmailOperator
from datetime import datetime


@dag(
    dag_id="send_email_dag",
    start_date=datetime(2026, 2, 1),
    schedule=None,
    catchup=False,
)
def send_email_dag():

    send_email_task = EmailOperator(
        task_id="send_email_task",
        to="abc@gmail.com",                   # recipient email
        subject="Airflow 3 EmailOperator Test",     # email subject
        html_content="<h3>Hello from Airflow 3!</h3>",  # email body
        conn_id="smtp_default"                      # make sure this connection is set correctly
    )

    send_email_task

send_email_dag()
