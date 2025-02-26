from fastapi import APIRouter
from .schemas import RequestStatus, ResponseStatus, ResponseStatusConsult, Status

status_router = APIRouter(prefix="/status")


@status_router.post("/update-status")
async def update_status(request: RequestStatus):
    return ResponseStatus(
        key_path="key_path", 
        file_id=request.file_id, 
        dest_path="dest_path", 
        status=request.status
    )


@status_router.get("/consult-status")
async def consult_status(request: RequestStatus):
    file_id = request.file_id
    return ResponseStatusConsult(
        Status=Status.processing, 
        details="details of processing file", 
        file_id=file_id
    )