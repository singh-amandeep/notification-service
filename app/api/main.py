from fastapi import FastAPI
from app.api.v1.endpoints import email

app = FastAPI(title="Notification Service")

app.include_router(email.router, prefix="/v1/notify", tags=["email"])
