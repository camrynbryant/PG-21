import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .models import model_loader
from .routers import index as indexRoute
import os

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_loader.index()
indexRoute.load_routes(app)

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("app_host"), port=int(os.getenv("app_port")))