from airflow.sdk import dag, task
from airflow.providers.standard.operators.bash import BashOperator

from datetime import datetime, timedelta


default_args = {
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    'execution_timeout': timedelta(seconds=300)
}
@dag(
    dag_id='basic_dag', 
    default_args=default_args,
    description='',
    schedule=None,
    start_date=datetime(2026, 2, 1),
    catchup=False,
    tags=["kai", "batch10"]
)
def basic_dag():

    @task.bash(
        task_id = 'say_hello_world'
    )
    def say_hello_world_task():
        return 'echo "Hello Pakistan"'
    
    say_hello_world_task = say_hello_world_task()

    say_hello_world_task

basic_dag()