from airflow.sdk import dag, task
from datetime import datetime, timedelta


default_args = {
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=3),
    "execution_timeout": timedelta(seconds=300),
}


@dag(
    dag_id="python_operator_dag",
    default_args=default_args,
    description="A simple tutorial DAG",
    schedule=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["kai", "batch10"],
)
def python_operator_dag():

    @task(task_id="say_welcome")
    def save_greeting_message(user, ti=None):

        message = f"Welcome {user} to airflow class"

        ti.xcom_push(key="message", value=message)


    @task(task_id="get_welcome_message")
    def get_greeting_message(**kwargs):

        message = kwargs['ti'].xcom_pull(task_ids='say_welcome', key="message")

        print(message)


    # Create task instances with same op_kwargs behavior
    t1 = save_greeting_message(user="zain.khan")
    t2 = get_greeting_message()

    # Same dependency
    t1 >> t2


python_operator_dag()
