
FROM jupyter/scipy-notebook:33add21fab64
COPY de-task-notebook.ipynb ./de-task-notebook.ipynb

RUN pip3 install psycopg2-binary && jupyter nbconvert --to notebook --execute de-task-notebook.ipynb
