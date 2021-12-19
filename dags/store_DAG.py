from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.mysql_operator import MySqlOperator
from cheapshark import getDealGameData,getStoreData

yesterday_date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')

default_args = {
    'owner': 'Airflow',
    'start_date': datetime(2021, 12, 13),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

with DAG('store_dag',default_args=default_args,schedule_interval='@daily', template_searchpath=['/usr/local/airflow/sql_files'], catchup=True) as dag:

    t1 = MySqlOperator(task_id='create_mysql_table', mysql_conn_id="mysql_conn2", sql="create_table.sql")
    t2 = PythonOperator(task_id='gen_store_csv', python_callable=getStoreData)
    t3 = PythonOperator(task_id='gen_dealgame_csv', python_callable=getDealGameData)
    t4 = MySqlOperator(task_id='insert_store_game_deal', mysql_conn_id="mysql_conn2", sql="insert_into_table.sql")
    
    t1 >> [t2,t3] >> t4 
