from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG
from datetime import datetime, timedelta

from airflow.sdk import dag, task
from datetime import datetime, timedelta


default_args = {
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "execution_timeout": timedelta(seconds=300),
}


@dag(
    dag_id="dag_scheduling",
    default_args=default_args,
    description="A simple tutorial DAG",
    schedule="*/1 * * * *",   # same schedule
    start_date=datetime(2025, 1, 1),  # same start_date
    catchup=False,
    tags=["kai", "batch10"],
)
def dag_scheduling():

    @task.bash(
        task_id="say_hello_world"
    )
    def say_hello_world_task():
        return 'echo "Hello World"'   # same command, unchanged

    say_hello_world_task()


dag_scheduling()