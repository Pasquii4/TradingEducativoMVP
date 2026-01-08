from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.config import settings
from app.utils.logger import setup_logger
from app.scheduler.tasks import start_scheduler, stop_scheduler
import logging

setup_logger()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Backend starting...")
    start_scheduler()
    yield
    logger.info("🛑 Backend shutting down...")
    stop_scheduler()

app = FastAPI(
    title="Trading Educativo MVP",
    description="AI-powered trading scanner + portfolio manager",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"status": "ok", "version": "0.1.0"}

@app.get("/")
async def root():
    return {
        "app": "Trading Educativo MVP",
        "status": "running",
        "docs": "/docs",
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
