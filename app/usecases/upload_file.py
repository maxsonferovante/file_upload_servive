import uuid
from app.core.config import get_logger
from app.api.v1.schemas import RequestUpload, ResponseUpload, URLPresigned
from app.services.s3_service import S3Service

logger = get_logger(__name__)

class UploadFile:
    def __init__(self, s3_service: S3Service):
        self.s3_service = s3_service

    def execute(self, data: RequestUpload) -> ResponseUpload:                
        responseUpload = ResponseUpload(list_urls=[])    
        for file in data.files:
            result = self.s3_service.generate_presigned_url(object_name=file.name)
            responseUpload.list_urls.append(
                URLPresigned(
                    fields=result,
                    file_id=str(uuid.uuid4()),
                    file_name=file.name
                )
            )
        logger.info(f'Presigned URL generated for object {data.files.__len__()}')        
        return responseUpload


        
        
        