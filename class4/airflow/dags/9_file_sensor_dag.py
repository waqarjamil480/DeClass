from datetime import datetime, timedelta
from airflow.sdk import dag, task
from airflow.sensors.filesystem import FileSensor

@dag(
    dag_id='file_sensor_dag',
    start_date=datetime(2025, 8, 15),
    schedule=None,
    catchup=False,
    default_args={
        'owner': 'airflow',
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
    tags=['file', 'sensor']
)
def file_sensor_dag():

    wait_for_file = FileSensor(
        task_id='wait_for_file',
        filepath='/opt/airflow/dags/files/input_data.txt',
        poke_interval=10,
        timeout=600,
        mode='reschedule',        # frees worker
        fs_conn_id='fs_default',  # optional if absolute path
    )

    @task
    def process_file():
        with open('/opt/airflow/dags/files/input_data.txt', 'r') as f:
            data = f.read()
            print(data)
            return data

    file_data = process_file()
    wait_for_file >> file_data

file_sensor_dag()
