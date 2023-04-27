from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'Dieisson',
    'depends_on_past': False,
}

dag = DAG(
    "piloto",
    description="Primeira DAG de teste",
    default_args=default_args,
    schedule="1 * * * *",
    tags=['primeira', 'teste'],
    catchup=False,
    start_date=datetime(2023, 4, 26)
)


def run():
    print('runting process...')


run = PythonOperator(
    task_id="run_pilot",
    python_callable=run,
    dag=dag
)

run_bash = BashOperator(
    task_id="run_pilot_bash",
    bash_command="echo 'runting process...'",
    dag=dag
)

run >> run_bash
