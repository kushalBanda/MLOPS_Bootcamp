"""
Apache Airflow introduced the TaskFlow API which allows you to create tasks 
using Python decorators like @task. This is a cleaner and more intutive way 
of writing tasks without needing to manually use operators like PythonOperator.
"""

from airflow import DAG 
from airflow.decorators import task
from datetime import datetime

# Define the DAG 
with DAG(
    dag_id = 'math_sequence_dag_with_taskflow',
    start_date = datetime(2023 ,1, 1),
    schedule_interval = '@once',
    catchup = False,
) as dag:
    

    # Task 1: Start with the Initial number
    @task
    def start_number():
        initial_number = 10
        print(f'Starting number is: {initial_number}')
        return initial_number
    
    # Task 2: Add 5 to the initial number
    @task
    def add_five(number):
        new_value = number + 5
        print(f'Adding 5 to the initial number: {number}')
        return new_value
    
    # Task 3: Multiply the result by 3
    @task
    def multiply_by_three(number):
        new_value = number * 3
        print(f'Multiplying the result by 3: {number}')
        return new_value
    
    # Task 4: Subtract 10 from the result
    @task
    def subtract_ten(number):
        new_value = number - 10
        print(f'Subtracting 10 from the result: {number}')
        return new_value
    
    # Task 5: Divide the result by 2
    @task
    def divide_by_two(number):
        new_value = number / 2
        print(f'Dividing the result by 2: {number}')
        return new_value
    
    # Set task dependencies
    start_value = start_number()
    added_values = add_five(start_value)
    multiplied_values = multiply_by_three(added_values)
    subtracted_values = subtract_ten(multiplied_values)
    final_value = divide_by_two(subtracted_values)
