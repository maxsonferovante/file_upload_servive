import logging
from pydantic_settings import BaseSettings


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


class Config(BaseSettings):
    KEY_ACCESS: str
    KEY_SECRET: str
    REGION: str
    BUCKET_NAME: str    

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"        


config = Config()


