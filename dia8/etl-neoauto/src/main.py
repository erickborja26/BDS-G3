from tasks.task_prueba import task_prueba
from prefect import flow

@flow(name="ETL Prueba")
def main_flow():
    task_prueba()
    
if __name__ == "__main__":
    main_flow()