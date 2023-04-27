# Nova taskflow API
from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {
    'owner': 'Dieisson',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 26)
}


@dag(
    default_args,
    schedule="*/1 * * * *",
    description="Teste taskflow API",
    catchup=False,
    tags=['primeira', 'teste']
)
def run():
    @task()
    def start():
        print('start process')

    @task()
    def say_today():
        today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(today)
        return today
