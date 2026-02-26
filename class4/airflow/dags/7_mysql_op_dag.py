from airflow.sdk import dag, task
from airflow.providers.mysql.hooks.mysql import MySqlHook
from datetime import datetime, timedelta
#in setting > connection > mysql > host=host.docker.internal

MYSQL_CONN_ID = "my_mysql_conn"

default_args = {
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=3),
    "execution_timeout": timedelta(seconds=300),
}

@dag(
    dag_id="mysql_operator_dag_7",
    default_args=default_args,
    description="A simple tutorial DAG",
    schedule=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["kai", "batch10"],
)
def mysql_operator_dag():
    
    hook = MySqlHook(mysql_conn_id=MYSQL_CONN_ID)

    @task(task_id="create_table")
    def run_query():
        hook.run("CREATE TABLE IF NOT EXISTS fruits(id INT, name VARCHAR(50));")


    @task(task_id="insert_data")
    def insert_tuples():
    
        data = [
            (1, "apple"),
            (2, "banana"),
            (3, "strawberry"),
        ]

        hook.insert_rows(
            table="fruits",
            rows=data,
            target_fields=["id", "name"],
            commit_every=1000,
        )


    @task(task_id="select_data")
    def read_fruits():
        sql = "SELECT * FROM fruits;"
        results = hook.get_records(sql)
        print("Fruits table contents:", results)


    @task(task_id="update_data")
    def update_fruit():
        sql = "UPDATE fruits SET name=%s WHERE id=%s"
        hook.run(sql, parameters=("green apple", 1), autocommit=True)


    @task(task_id="delete_data")
    def delete_fruit():
        sql = "DELETE FROM fruits WHERE id=%s"
        hook.run(sql, parameters=(2,), autocommit=True)


    # Create task instances
    t1 = run_query()
    t2 = insert_tuples()
    t3 = read_fruits()
    t4 = update_fruit()
    t5 = delete_fruit()

    # Same execution order preserved
    t1 >> t2 >> t3 >> t4 >> t5


mysql_operator_dag()
