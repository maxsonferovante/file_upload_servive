# Definição dos modelos de request/response da API

from enum import Enum
from typing import Optional, List
from pydantic import BaseModel


class TypeFile(str,Enum):
    sped = 'sped'


class File(BaseModel):
    name: str
    type: TypeFile = TypeFile.sped
    size: int
    extension: str

class RequestUpload(BaseModel):
    files: List[File]    


class URLPresigned(BaseModel):
    fields: dict
    file_id: str
    file_name: str

class ResponseUpload(BaseModel):
    list_urls: List[URLPresigned]  


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