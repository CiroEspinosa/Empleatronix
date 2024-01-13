FROM python:3.8

RUN pip install streamlit matplotlib pandas

COPY src/app.py /app/
COPY data/employees.csv /app/

WORKDIR /app

ENTRYPOINT ["streamlit", "run", "app.py"]

