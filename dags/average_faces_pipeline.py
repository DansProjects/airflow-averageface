from airflow import DAG
from airflow.operators import PythonOperator, BashOperator
from datetime import datetime, timedelta

# Following are defaults which can be overridden later on
default_args = {
    'owner': 'dan',
    'depends_on_past': False,
    'start_date': datetime(2017, 10, 8),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('AverageFacePipeline', default_args=default_args)


def print_starting():
    print('Airflow pipeline starting!')


def print_finished():
    print('Airflow pipeline finished!')


def print_scrape_in_progress():
    print('Scraped is in progress!')

# many placeholders for now

t1 = PythonOperator(
    task_id='task_1',
    python_callable=print_starting,
    dag=dag)

t2 = BashOperator(
    task_id='task_2',
    bash_command='cd /Users/dmo/Documents/python/airflow && scrapy crawl csgrad',
    dag=dag)

t3 = PythonOperator(
    task_id='task_3',
    python_callable=print_scrape_in_progress,
    dag=dag)

t4 = BashOperator(
    task_id='task_4',
    bash_command='ls',
    dag=dag)

t5 = PythonOperator(
    task_id='task_5',
    python_callable=print_finished,
    dag=dag)

t2.set_upstream(t1)
t3.set_upstream(t1)
t4.set_upstream(t2)
t4.set_upstream(t3)
t5.set_upstream(t4)