import time
import uvicorn
from fastapi import FastAPI
from app.config.celery_conifg import celery
from app.routers import routes


def create_app() -> FastAPI:
    current_app = FastAPI(title="POC ML WEB API",
                          description="Sample FastAPI Application to demonstrate Event driven ML"
                                      "architecture with Celery and RabbitMQ",
                          version="1.0.0", )

    current_app.celery_app = celery
    current_app.include_router(routes.router)
    return current_app


app = create_app()
celery = app.celery_app


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)