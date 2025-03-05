import uvicorn
from fastapi import FastAPI

import models.models
from database import engine
from routers import fart


models.models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(fart.router)


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
