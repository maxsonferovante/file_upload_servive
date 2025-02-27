import os
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.core.config import get_logger

logger = get_logger(__name__)

from .schemas import RequestUpload, ResponseStatus, ResponseUpload
from app.compose.upload_compose import upload_compose


upload_router = APIRouter(prefix="/uploads")


@upload_router.post("/upload")
async def upload_file(request: RequestUpload) -> ResponseUpload:
    upload_file = upload_compose()    
    response = upload_file.execute(request)    
    return response



@upload_router.post("/confirm-upload")
async def confirm_upload(file_id: str) -> ResponseStatus:
    return ResponseStatus(
        file_id=file_id,
        key_path="123456",
        dest_path="https://www.example.com/upload",
    )
    

@upload_router.get("/forms", response_class=HTMLResponse)
async def get_forms():
    """
    Lê o arquivo forms.html da pasta static e retorna como resposta HTML.
    """
    forms_file = os.path.join(os.getcwd(), "static", "forms.html")
    with open(forms_file, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)