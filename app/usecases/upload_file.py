import uuid
from app.core.config import get_logger
from app.api.v1.schemas import RequestUpload, ResponseUpload
from app.services.s3_service import S3Service

logger = get_logger(__name__)

class UploadFile:
    def __init__(self, s3_service: S3Service):
        self.s3_service = s3_service

    def execute(self, data: RequestUpload) -> ResponseUpload:        
        
        logger.info('Executing upload file use case for object {}'.format(data.file))
        
        result = self.s3_service.generate_presigned_url(object_name=data.file)
        
        return ResponseUpload(
            upload_url=result,
            file_id=str(uuid.uuid4()),
            file_name=data.file
        )