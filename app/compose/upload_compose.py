
from app.services.s3_service import S3Service
from app.usecases.upload_file import UploadFile


def upload_compose() -> UploadFile:
    s3_service = S3Service()
    upload_file = UploadFile(s3_service)
    return upload_file    