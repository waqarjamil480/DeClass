from airflow.sdk import dag, task
from datetime import datetime, timedelta


default_args = {
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=3),
    "execution_timeout": timedelta(seconds=300),
}


@dag(
    dag_id="xcom_bash_dag_5",
    default_args=default_args,
    description="A simple tutorial DAG",
    schedule=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["kai", "batch10"],
)
def xcom_bash_dag():

    @task.bash(
        task_id="save_bash_data_xcom"
    )
    def save_bash_data_xcom_task():
        return 'echo "Hello Xcom. This is my second push"'
        # this will save the value in xcom key "save_bash_data_xcom"


    @task.bash(
        task_id="load_bash_data_xcom"
    )
    def load_bash_data_xcom_task():
        #used the key define above for xcom and now by calling key "save_bash_data_xcom" it will show saved value from xcom
        return "echo '{{ ti.xcom_pull(\"save_bash_data_xcom\") }}'"


    # Create task instances
    t1 = save_bash_data_xcom_task()
    t2 = load_bash_data_xcom_task()


    # Same dependency
    t1 >> t2

xcom_bash_dag()
