from airflow import DAG 
from airflow.operators.python import PythonOperator
from datetime import datetime 

# Task 1: Preprocess
def preprocess_data():
    print('Preprocessed Data...')

# Task 2: Train
def train_model():
    print("Training model...")

# Task 3: Evaluate
def evaluate_model():
    print("Evaluate model...")

# Define the DAG
with DAG(
    dag_id='MLpipeline',  # DAG name
    start_date=datetime(2025, 6, 15),
    schedule='@weekly',  # Use 'schedule' instead of 'schedule_interval'
    catchup=False
) as dag:
    
    preprocess = PythonOperator(
        task_id='preprocess_task',
        python_callable=preprocess_data
    )

    train = PythonOperator(
        task_id='train_task',
        python_callable=train_model
    )

    evaluate = PythonOperator(
        task_id='evaluate_task',
        python_callable=evaluate_model
    )

    # Set task dependencies
    preprocess >> train >> evaluate
