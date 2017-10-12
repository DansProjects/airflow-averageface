from airflow import DAG
from airflow.operators import PythonOperator, BashOperator
from datetime import datetime, timedelta
import os

# Following are defaults which can be overridden later on
default_args = {
    'owner': 'Dan M',
    'depends_on_past': False,
    'start_date': datetime(2017, 10, 11),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=1),
}

cspeople_scraper = '/Users/dmo/Documents/python/airflow'
cspeople_scraper_path = '/Users/dmo/Documents/python/airflow/cspeople/scraped/full'
averageface_path = '/Users/dmo/Documents/python/airflow/averageface/'


dag = DAG('AverageFacePipeline', default_args=default_args)


def clear_folder(dir_path=cspeople_scraper_path):

    file_list = os.listdir(dir_path)
    for file_name in file_list:
        if file_name.endswith('.jpg') or file_name.endswith('.txt'):
            os.remove(dir_path + "/" + file_name)


def print_scrape_in_progress():
    print('Scraped is in progress!')

# delete all jpg and txt files in the scraped folder
t1 = PythonOperator(
    task_id='clear_scrape_folder',
    python_callable=clear_folder,
    dag=dag)

# TODO properly import python classes
t2 = BashOperator(
    task_id='scrape_profile_images',
    bash_command='cd {} && scrapy crawl csgrad'.format(cspeople_scraper),
    dag=dag)

t3 = PythonOperator(
    task_id='scrape_progress',
    python_callable=print_scrape_in_progress,
    dag=dag)

t4 = BashOperator(
    task_id='create_landmarks',
    bash_command='cd {} && python landmark.py'.format(averageface_path),
    dag=dag)

t5 = BashOperator(
    task_id='create_average_face',
    bash_command='cd {} && python averageface.py'.format(averageface_path),
    dag=dag)

t2.set_upstream(t1)
t3.set_upstream(t1)
t4.set_upstream(t2)
t4.set_upstream(t3)
t5.set_upstream(t4)