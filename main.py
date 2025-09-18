"""FastAPI application for papercheck_db."""

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from papercheck_db.core.config import settings
from papercheck_db.core.database import get_db

app = FastAPI(
    title="PaperCheck DB API",
    description="Config and API for papercheck database -> datasets, papers, extractors, extractor evaluations",
    version="0.1.0",
    debug=settings.is_development,
)


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "PaperCheck DB API",
        "version": "0.1.0",
        "environment": settings.environment
    }


@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    """Health check endpoint."""
    try:
        # Test database connection
        db.execute("SELECT 1")
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "error", "error": str(e)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.is_development
    )