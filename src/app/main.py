from fastapi import FastAPI

from app.api import insight

app = FastAPI(title="fastapi-ai-backend")
app.include_router(insight.router, prefix="/insight")


@app.get("/")
def root():
    """
    root api endpoint for the fastapi-ai-backend app
    :return: name of the backend app
    """
    return {"app_name": "fastapi-ai-backend"}
