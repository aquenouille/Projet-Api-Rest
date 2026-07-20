from fastapi import FastAPI
from app.routers import employees, tasks
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="HR Workflows API",
    description="API de gestion d'onboarding d'employés avec taches",
    version="1.0"
)

app.include_router(employees.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "HR Workflows API is running"}