from fastapi import FastAPI
from app.routers import crossings, status

app = FastAPI(title="Railway Crossing Status API")

app.include_router(crossings.router)
app.include_router(status.router)
