# 1.Realty_price_predict

Streamlit
```
streamlit run main.py
```


- Mlflow
```
pip install mlflow

export MLFLOW_REGISTRY_URI=mlflow

Запуск сервера: mlflow server --host localhost --port 5000 --backend-store-uri sqlite:///${MLFLOW_REGISTRY_URI}/mlflow.db --default-artifact-root ${MLFLOW_REGISTRY_URI}
```

- Airflow
```
pip install apache-airflow==2.8.1 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.8.txt"

export AIRFLOW_HOME=~/IT/DS_practice/4.CV/1.Similar_to_actor/airflow

airflow db init

airflow.cfg прописать:
[webserver] rbac = True
load_examples = False

airflow users create --username geramond --firstname Maksim --lastname Fomin --role Admin --email geramond@gmail.com

airflow webserver -p 8080

airflow scheduler
```

- FastAPI
```
python3 -m uvicorn main:app --host=127.0.0.1 --port 8000 --reload
```





