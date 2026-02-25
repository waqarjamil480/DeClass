from airflow.sdk import dag, task
from airflow.providers.standard.operators.bash import BashOperator

from datetime import datetime, timedelta
 
# default arguments
default_args = {
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(seconds=5),
    'execution_timeout': timedelta(seconds=300)
}
# define DAG using decorator (Airflow 3 style)
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

    #task for bash sciprt like we have task for email
    # bash for bash command not for python currently
    @task.bash(
        task_id = 'say_hello_world'
    )
    def say_hello_world_task():
        return 'echo "Hello Pakistan"'
    
    say_hello_world_task = say_hello_world_task()

    say_hello_world_task

basic_dag()
#cron tab guru