from airflow.sdk import dag, task
from datetime import datetime, timedelta


default_args = {
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "execution_timeout": timedelta(seconds=300)
}


@dag(
    dag_id="dag_execution_order",
    default_args=default_args,
    description="A simple tutorial DAG",
    schedule=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["kai", "batch10"],
)
def dag_execution_order():

    @task.bash(task_id="say_hello_world")
    def say_hello_world_task():
        return 'echo "Hello World"'


    @task.bash(task_id="say_hello_pakistan")
    def say_hello_pakistan_task():
        return 'echo "Hello Pakistan"'


    @task.bash(task_id="say_hello_karachi")
    def say_hello_karachi_task():
        return 'echo "Hello Karachi"'


    @task.bash(task_id="say_hello_usa")
    def say_hello_usa_task():
        return 'echo "Hello USA"'


    # Create task instances
    t1 = say_hello_world_task()
    t2 = say_hello_pakistan_task()
    t3 = say_hello_karachi_task()
    t4 = say_hello_usa_task()


    # Same dependency structure as original DAG
    t1 >> [t2, t3] >> t4
    # t2 >> t4
    # t3 >> t4


dag_execution_order()
