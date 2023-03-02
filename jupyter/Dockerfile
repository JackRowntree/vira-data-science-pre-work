
FROM jupyter/scipy-notebook:33add21fab64
WORKDIR /code
COPY . .
RUN pip3 install psycopg2-binary && jupyter trust de-task-notebook.ipynb 