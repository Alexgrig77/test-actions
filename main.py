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


@app.get("/date")
async def get_current_date():
    """Возвращает текущую дату сервера"""
    current_date = datetime.now()
    return {
        "date": current_date.date().isoformat(),
        "year": current_date.year,
        "month": current_date.month,
        "day": current_date.day,
        "weekday": current_date.strftime("%A")
    }

