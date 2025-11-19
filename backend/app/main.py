from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import engine, Base, get_db

# Import database models
from app.models import User, Project, Task

# Import routers
from app.routers import auth, users, projects, tasks

# NOTE: We're using Alembic for migrations now
# Run migrations with: alembic upgrade head

app = FastAPI(
    title="Project Management API",
    description="A full-stack project management system",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(projects.router)
app.include_router(tasks.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Project Management API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Test database connection endpoint
@app.get("/db-test")
async def test_db(db: Session = Depends(get_db)):
    """
    Test endpoint to verify database connection is working.
    """
    try:
        result = db.execute(text("SELECT 1"))
        return {
            "status": "success",
            "message": "Database connection successful",
            "result": result.scalar()
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Database connection failed: {str(e)}"
        }