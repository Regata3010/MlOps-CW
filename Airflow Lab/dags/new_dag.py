from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


def load_data():
    """Task 1: Load data"""
    print("📊 Loading data...")
    # Simulate data loading
    data = {'records': 1000, 'status': 'loaded'}
    print(f"✅ Loaded {data['records']} records")
    return data

def process_data(**context):
    """Task 2: Process the data"""
    print("⚙️ Processing data...")
    
    ti = context['ti']
    data = ti.xcom_pull(task_ids='load_data_task')
    print(f"   Processing {data['records']} records")
    
    
    processed_data = {'records': data['records'], 'status': 'processed'}
    print("✅ Data processed successfully")
    return processed_data

def train_model(**context):
    """Task 3: Train a model"""
    print("🤖 Training model...")
    
    ti = context['ti']
    data = ti.xcom_pull(task_ids='process_data_task')
    print(f"   Training on {data['records']} records")
    
    
    model_metrics = {
        'accuracy': 0.92,
        'precision': 0.89,
        'recall': 0.91
    }
    print(f"✅ Model trained: Accuracy={model_metrics['accuracy']}")
    return model_metrics

def evaluate_and_save(**context):
    """Task 4: Evaluate and save results"""
    print("💾 Evaluating and saving...")
    
    ti = context['ti']
    metrics = ti.xcom_pull(task_ids='train_model_task')
    
    if metrics['accuracy'] > 0.85:
        print(f"✅ Model PASSED with accuracy {metrics['accuracy']}")
        status = "deployed"
    else:
        print(f"❌ Model needs improvement: {metrics['accuracy']}")
        status = "rejected"
    
    print(f"   Final status: {status}")
    return status


default_args = {
    'owner': 'student',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

# Create the DAG
dag = DAG(
    'simple_ml_pipeline',
    default_args=default_args,
    description='Simple ML Pipeline for Lab',
    schedule_interval=None,  # Manual trigger only
    catchup=False,
    tags=['lab', 'ml', 'simple']
)

# Define tasks
load_task = PythonOperator(
    task_id='load_data_task',
    python_callable=load_data,
    dag=dag
)

process_task = PythonOperator(
    task_id='process_data_task',
    python_callable=process_data,
    provide_context=True,
    dag=dag
)

train_task = PythonOperator(
    task_id='train_model_task',
    python_callable=train_model,
    provide_context=True,
    dag=dag
)

evaluate_task = PythonOperator(
    task_id='evaluate_save_task',
    python_callable=evaluate_and_save,
    provide_context=True,
    dag=dag
)


load_task >> process_task >> train_task >> evaluate_task

