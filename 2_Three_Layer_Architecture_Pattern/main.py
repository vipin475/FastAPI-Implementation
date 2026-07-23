from fastapi import FastAPI
from web import router

app = FastAPI(title="Task API with Architecture", version="1.0.0")
app.include_router(router)