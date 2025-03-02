from app.services.boto_aws import ServiceNameAWS, get_instance_aws
from app.core.config import config, get_logger
from typing import Dict
logger = get_logger(__name__)

class S3Service:
    def __init__(self):
        self.aws = get_instance_aws(
            ServiceNameAWS.S3
        )
        self.bucket_name = config.BUCKET_NAME

    # gerar um link pre-assinado
    def generate_presigned_url(self, object_name: str, expiration: int = 3600) -> Dict:
        try:
            response = self.aws.generate_presigned_post(
                Bucket=self.bucket_name,
                Key=object_name,
                Fields={"Content-Type": "application/octet-stream"},
                Conditions=[
                    {"Content-Type": "application/octet-stream"}
                ],
                ExpiresIn=expiration                
            )
            logger.info(f'Presigned URL generated for object {object_name}')
            return response
        except Exception as e:
            logger.error(f'Error generating presigned URL for object {object_name}')
            raise e
    