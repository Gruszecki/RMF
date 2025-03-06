import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models.models
from database import engine
from routers import fart


models.models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(fart.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
