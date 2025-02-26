from fastapi import APIRouter
from .schemas import RequestUpload, ResponseStatus, ResponseUpload

upload_router = APIRouter(prefix="/uploads")


@upload_router.post("/upload")
async def upload_file(request: RequestUpload, response: ResponseUpload) -> ResponseUpload:
    return ResponseUpload(
        upload_url="https://www.example.com/upload",
        file_id="123456",
        file_name=request.file,
    )



@upload_router.get("/confirm-upload")
async def confirm_upload(file_id: str) -> ResponseStatus:
    return ResponseStatus(
        file_id=file_id,
        key_path="123456",
        dest_path="https://www.example.com/upload",
    )
    