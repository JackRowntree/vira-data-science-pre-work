# Repo contents 

- Notebook in `/jupyter`. Open `jupyter/de-task-notebook.ipynb` for a full summary of the solution, and data exploration code.

- Dashboard code in `/app`

- Database Dockerfile in `/db`

# Summary

Overall, I approached this task as follows:
    
1. Explore dataset in Jupyter/Excel
2. Use this to educate development of data processing functions in Jupyter
3. Set up postgres db in Docker container
4. Sketch out an ETL that loads data to postgres
5. Develop Dash app in Jupyter environment using JupyterDash
6. Set up Dash app in a seperate container that sends query requests to db container

The goal was to provide theoretical data consumers with sufficiently processed data (e.g. null values standardised, datetimes converted) to generate more engineering requirements. The features of the data quality dashboard could be used in conjunction with the data itself to educate this process.


The database and dashboard are each hosted in docker containers, to easily deploy/scale up in a theoretical production environment.

# Running Locally


1. Make sure you have Docker installed on your machine
2. docker-compose up db to spin up the postgres service, which will be available at `127.0.0.1:5433`
3. `cd` into `./jupyter`
4. Create a new virtual env `python3 -m venv ./vira-task-env`
5. Activate the virtual env `source ./vira-task-env/bin/activate` and `pip install jupyter`
6. Add kernel to jupyter environment `ipython kernel install --name "vira-kernel" --user` 
7. `jupter notebook`, select `vira-kernel` kernel, and run cells.
8. `docker-compose up dashboard` to spin up the dash service.
9. Open the dash service in browser at `0.0.0.0/8000`


