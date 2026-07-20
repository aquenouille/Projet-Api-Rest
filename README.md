# Workflows API REST

Learning work : API

## Description
Learning project - building a REST API to create and manage employees database. is possible to create employees, create and assign tasks and delete them

## Languages and tools 

- **Python** : main programming language
- **FastAPI** : framework to build API 
- **PostgreSQL** : database
- **SQLAlchemy** : Python package to interact with PostgreSQL
- **Pydantic** : modele to validate data
- **Docker** : run PostgreSQL locally from a terminal
- **Uvicorn** : web server


## How to start

Need dependencies of python

### Requirements

- Python3 3.12 and more
- Docker 

### Installation

Clone the repository : 

```bash
git clone <url> 
cd projet1_apirest
```

### Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

All python libraries used for the API are in teh requirements.txt
```bash
pip install -r requirements.txt
```

### Create the .env file

.env is a file that contains hidden informatiosn as password.
Create it at the root of the project : 
```
DATABASE_URL=postgresql://<user>:<password>@localhost:5432/<database_name>
```

Replace :
- `<user>` with your PostgreSQL username
- `<password>` with your PostgreSQL password
- `<database_name>` with your database name

### Start PostgreSQL with Docker

```bash
docker run --name postgres-dev -e POSTGRES_PASSWORD=<password> -e POSTGRES_USER=<admin> -e POSTGRES_DB=<database_name> -p 5432:5432 -d postgres
```

### Start API

```
fastapi dev app/main.py
```

## Endpoints

Endpoints

### Employees
- POST /employees --> create an employee
- GET /employees → list all employees
- GET /employees/{id} → get an employee by id

### Tasks
- POST /tasks/ → create a task and assign it to an employee
- GET /tasks/employee/{id} → list tasks of an employee
- PATCH /tasks/{id} → udate task status
- DELETE /tasks/{id} → delete a task


## What I learned

- REST API concepts : endpoints, HTTP verbs, Pydantic models
- Build an API with FastAPI in Python
- Connect an API to a PostgreSQL database with SQLAlchemy
- Separate code into multiple files with inheritance
- Use Docker to run PostgreSQL locally
- Test endpoints using the auto-generated /docs interface

## Next steps

- add automated tests with pytest