import uvicorn
from fastapi import FastAPI
from loguru import logger

from app.config import settings
from app.routes.message_router import router as message_router
from app.db.database import init_db

app = FastAPI(title="Expense Bot Service")

@app.on_event("startup")
async def startup_event():
    logger.info("Initializing database connection...")
    await init_db()
    logger.info("Database connection initialized")

app.include_router(message_router, prefix="/api")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    logger.info(f"Starting server on port {settings.api_port}")
    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.api_port, reload=True)