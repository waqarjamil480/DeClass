from airflow.sdk import dag, task
from datetime import datetime, timedelta


default_args = {
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=3),
    "execution_timeout": timedelta(seconds=300),
}


@dag(
    dag_id="python_via_bash_dag",
    default_args=default_args,
    description="A simple tutorial DAG",
    schedule=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["kai", "batch10"],
)
def python_via_bash_dag():

    @task.bash(task_id="say_hello_world")
    def say_hello_world_task():
        return 'python3 -c "print(\'Hello from Python inside BashOperator\')"'

    @task.bash(task_id="say_hello_world_file_task")
    def say_hello_world_file_task():
        return "python3 /opt/airflow/dags/hello.py"

    @task.bash(task_id="word_count")
    def word_count_task():
        return "wc -w /opt/airflow/dags/hello.py"

    @task.bash(task_id="line_count")
    def line_count_task():
        return "wc -l /opt/airflow/dags/hello.py"

    @task.bash(task_id="chars_count")
    def chars_count_task():
        return "wc -c /opt/airflow/dags/hello.py"

    @task.bash(task_id="rename_file")
    def rename_file_task():
        return "mv /opt/airflow/dags/to_be_renamed /opt/airflow/dags/valid_file"


    # Execute tasks (no dependency defined in original DAG, so keeping same behavior)
    say_hello_world_task()
    say_hello_world_file_task()
    word_count_task()
    line_count_task()
    chars_count_task()
    rename_file_task()


python_via_bash_dag()
