from fastapi import APIRouter, BackgroundTasks
from pydantic import Emailstr
from app.services.email_service import send_email

router = APIRouter()

@router.post("/email")
async def send_email_endpoint(
    to: Emailstr,
    subject: str,
    body: str,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(send_email, to, subject, body)
    return {"message": "Email task submitted."}