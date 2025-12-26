from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Time Server API", version="1.0.0")


@app.get("/")
async def root():
    return {"message": "Time Server API is running"}


@app.get("/time")
async def get_current_time():
    """Возвращает текущее время сервера"""
    current_time = datetime.now()
    return {
        "server_time": current_time.isoformat(),
        "timestamp": current_time.timestamp()
    }

