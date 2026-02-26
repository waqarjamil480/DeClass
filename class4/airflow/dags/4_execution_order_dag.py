from airflow.sdk import dag, task
from datetime import datetime, timedelta
import time

default_args = {
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "execution_timeout": timedelta(seconds=300)
}


@dag(
    dag_id="dag_execution_order_4",
    default_args=default_args,
    description="A simple tutorial DAG",
    schedule=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["kai", "batch10"],
)
#we have added time sleep 3 beacuse this will show us the delay otherwise it will show all task too quickly
def dag_execution_order():

    @task.bash(task_id="say_hello_world")
    def say_hello_world_task():
        time.sleep(3)        
        return 'echo "Hello World"'


    @task.bash(task_id="say_hello_pakistan")
    def say_hello_pakistan_task():
        time.sleep(3)
        return 'echo "Hello Pakistan"'


    @task.bash(task_id="say_hello_karachi")
    def say_hello_karachi_task():
        time.sleep(3)
        return 'echo "Hello Karachi"'


    @task.bash(task_id="say_hello_usa")
    def say_hello_usa_task():
        time.sleep(3)
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


#    t1 >> [t2, t3]    try these too by uncomment
    # t2 >> t4
    # t3 >> t4



dag_execution_order()
