from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.upload_router import upload_router
from api.v1.status_router import status_router

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router, prefix="/api/v1")
app.include_router(status_router, prefix="/api/v1")