from datetime import datetime
from pathlib import Path
import subprocess
import sys

from airflow import DAG
from airflow.operators.python import PythonOperator


PROJECT_ROOT = Path(__file__).resolve().parent.parent
PIPELINE_SCRIPT = PROJECT_ROOT / "pipeline.py"


def ejecutar_pipeline():
    if not PIPELINE_SCRIPT.is_file():
        raise FileNotFoundError(
            f"No se encontro el pipeline: {PIPELINE_SCRIPT}"
        )

    subprocess.run(
        [sys.executable, str(PIPELINE_SCRIPT)],
        cwd=str(PROJECT_ROOT),
        check=True,
    )


with DAG(
    dag_id="pipeline_supermercado_diario",
    description="Ejecuta el pipeline ETL de Supermercado todos los dias",
    start_date=datetime(2024, 1, 1),
    schedule="0 2 * * *",
    catchup=False,
    tags=["supermercado", "etl", "duckdb"],
) as dag:
    ejecutar_etl = PythonOperator(
        task_id="ejecutar_pipeline",
        python_callable=ejecutar_pipeline,
    )