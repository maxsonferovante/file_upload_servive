# Definição dos modelos de request/response da API

from enum import Enum
from typing import Optional
from pydantic import BaseModel


class TypeFile(str,Enum):
    sped = 'sped'


class RequestUpload(BaseModel):
    file: str
    extension: str
    type: TypeFile = TypeFile.sped
    length: int


class ResponseUpload(BaseModel):
    upload_url: str
    file_id: str
    file_name: str


class Status(str, Enum):
    pending = 'pending'
    processing = 'processing'
    done = 'done'
    error = 'error'

class RequestStatus(BaseModel):
    file_id: str
    status: Optional[Status] = None

class ResponseStatus(BaseModel):
    key_path: str
    file_id: str
    dest_path: str
    status: Status = Status.pending

class ResponseStatusConsult(BaseModel):
    Status: Status
    details: str
    file_id: str