'''
Final Project

Nama     : Devon, Heru, Vincar
Kelompok : 002
Batch    : HCK-018

This program is designed to automate the process of loading data from Google Drive, 
preprocessing it to clean and transform it, exporting the processed data to a specific folder, 
and finally extracting the processed data into PostgreSQL.
'''

import pandas as pd
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator

# Define the Google Drive file link
file_url = 'https://drive.google.com/file/d/1vBuQFRwGeY50NOjXXLk1Pj8z5FZN_9N4/view?usp=sharing'

# Define default arguments for the DAG
default_args = {
    'owner': 'Heru',
    'start_date': datetime(2024, 8, 14) - timedelta(hours=7)  # Start Date set in WIB
}

with DAG(
    'FP_002_DAG_HCK',  # Project DAG Name
    description='Final_Project',  # Project DAG description
    schedule_interval='30 6 * * *',  # Schedule interval (6:30 AM daily)
    default_args=default_args,
    catchup=False  # Disables catchup (Airflow will not backfill missed runs)
) as dag:

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    # Define the function to read data from Google Drive and save it locally
    def read_from_gdrive(url, file_name):
        url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]  # Convert Google Drive link
        df = pd.read_csv(url)  # Read the data from the URL
        print("Sample data:")
        print(df.head())
        file_path = f'/opt/airflow/dags/{file_name}.csv'
        df.to_csv(file_path, index=False)  # Save the file locally
        return file_path  # Return the file path instead of the DataFrame

    @task()
    def get_file():
        file_name = 'FP_002_Bank_raw'
        file_path = read_from_gdrive(file_url, file_name)
        return file_path  # Return the path to the saved file

    @task()
    def preprocess_data(file_path):
        ''' 
        Function to clean the data by removing duplicates, handling missing values, 
        and standardizing column names.
        '''
        df = pd.read_csv(file_path)

        # Drop duplicates from dataframe
        df.drop_duplicates(inplace=True)

        # Drop rows with missing values
        df.dropna(inplace=True)
        
        # Function to add spaces between words in column names
        df.columns = df.columns.str.replace(r'([a-z])([A-Z])', r'\1 \2', regex=True)

        # Replace spaces with underscores in the column names
        df.columns = df.columns.str.replace(' ', '_')

        # Convert all column names to lowercase
        df.columns = df.columns.str.lower()

        # Remove any tab and newline characters from the column names
        df.columns = df.columns.str.replace(r'[\t\n]', '')

        # Save cleaned data to a new CSV file
        cleaned_file_path = '/opt/airflow/dags/FP_002_Bank_clean.csv'
        df.to_csv(cleaned_file_path, index=False)
        print("Preprocessed data saved successfully.")
        return cleaned_file_path  # Return the cleaned file path

    @task()
    def insert_to_db(cleaned_file_path):
        '''
        Function to extract the cleaned CSV data into Postgres.
        '''
        # Define PostgreSQL database connection parameters
        database = "airflow_fp"  # PostgreSQL database name
        username = "airflow_fp"  # Username for database authentication
        password = "airflow_fp"  # Password for database authentication
        host = "postgres"  # Hostname of the PostgreSQL server

        postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"
        engine = create_engine(postgres_url)

        # Load the cleaned data
        df = pd.read_csv(cleaned_file_path)

        # Write the DataFrame to a table in the PostgreSQL database
        df.to_sql('table_fp', engine, index=False, if_exists='replace')  # Replace table if it already exists
        print("Data inserted into Postgres successfully.")

    # Define task dependencies
    file_task = get_file()
    cleaned_file_task = preprocess_data(file_task)
    start >> file_task >> cleaned_file_task >> insert_to_db(cleaned_file_task) >> end
