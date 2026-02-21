from airflow.sdk import dag
from airflow.providers.http.operators.http import HttpOperator
from datetime import datetime, timedelta

@dag(
    dag_id='http_operator_dag',
    start_date=datetime(2025, 8, 15),
    schedule=None,
    catchup=False,
    default_args={
        'owner': 'airflow',
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
    tags=['http', 'api']
)
def http_operator_dag():

    get_posts = HttpOperator(
        task_id='get_posts',
        method='GET',
        http_conn_id='my_http_conn',             # must exist in Airflow Connections
        endpoint='quotes',                        # relative to base_url in connection
        headers={"Content-Type": "application/json"},
        response_filter=lambda response: response.json(),  # parse JSON response
        log_response=True,
        params={'page': 2}                       # query parameters
    )

    get_posts  # no need to call, just reference the operator

http_operator_dag()
