from fastapi import APIRouter
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



@upload_router.get("/confirm-upload")
async def confirm_upload(file_id: str) -> ResponseStatus:
    return ResponseStatus(
        file_id=file_id,
        key_path="123456",
        dest_path="https://www.example.com/upload",
    )
    