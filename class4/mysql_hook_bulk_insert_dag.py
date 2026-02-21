from airflow.sdk import DAG
from airflow.providers.mysql.hooks.mysql import MySqlHook
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

MYSQL_CONN_ID = 'my_mysql_conn'

def run_query(**kwargs):
    hook = MySqlHook(mysql_conn_id=MYSQL_CONN_ID)
    # Example query
    hook.run("CREATE TABLE IF NOT EXISTS fruits(id INT, name VARCHAR(50));")

def insert_tuples(**kwargs):
    hook = MySqlHook(mysql_conn_id=MYSQL_CONN_ID)
    
    # List of tuples to insert
    data = [
        (1, 'apple'),
        (2, 'banana'),
        (3, 'strawberry')
    ]
    
    # Insert using executemany
    # sql = "INSERT INTO fruits (id, name) VALUES (%s, %s)"
    
    # for row in data:
    #     hook.run(sql, parameters=row, autocommit=True)

    # to bulk insert tow
    hook.insert_rows(
        table="fruits",
        rows=data,
        target_fields=["id", "name"],
        commit_every=1000  # Batch commit size
    )


def read_fruits(**kwargs):
    hook = MySqlHook(mysql_conn_id=MYSQL_CONN_ID)
    sql = "SELECT * FROM fruits;"
    results = hook.get_records(sql)
    print("Fruits table contents:", results)

def update_fruit(**kwargs):
    hook = MySqlHook(mysql_conn_id=MYSQL_CONN_ID)
    sql = "UPDATE fruits SET name=%s WHERE id=%s"
    hook.run(sql, parameters=('green apple', 1), autocommit=True)

def delete_fruit(**kwargs):
    hook = MySqlHook(mysql_conn_id=MYSQL_CONN_ID)
    sql = "DELETE FROM fruits WHERE id=%s"
    hook.run(sql, parameters=(2,), autocommit=True)

with DAG(
    dag_id="mysql_operator_dag",
    default_args={
        "depends_on_past": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=3),
        'execution_timeout': timedelta(seconds=300),
        # 'on_failure_callback': some_function, # or list of functions
        # 'on_success_callback': some_other_function, # or list of functions
        # 'on_retry_callback': another_function, # or list of functions
        # 'trigger_rule': 'all_success'
    },
    description="A simple tutorial DAG",
    schedule=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["kai", "batch9"]
) as dag:
    create_table_task = PythonOperator(
        task_id="create_table",
        python_callable=run_query
    )

    insert_data_task = PythonOperator(
        task_id="insert_data",
        python_callable=insert_tuples
    )

    select_data_task = PythonOperator(
        task_id="select_data",
        python_callable=read_fruits
    )

    update_data_task = PythonOperator(
        task_id="update_data",
        python_callable=update_fruit
    )

    delete_data_task = PythonOperator(
        task_id="delete_data",
        python_callable=delete_fruit
    )

    create_table_task >> insert_data_task >> select_data_task >> update_data_task >> delete_data_task