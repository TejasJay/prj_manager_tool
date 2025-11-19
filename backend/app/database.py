from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
from pathlib import Path

# Get the backend directory path
backend_dir = Path(__file__).parent.parent

# Add backend directory to Python path
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

from config import settings

# Create SQLAlchemy engine
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,  # Automatically reconnect if connection is lost
    echo=True  # Set to False in production - shows SQL queries in console
)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all our database models
Base = declarative_base()

# Dependency to get database session
def get_db():
    """
    Dependency function that yields a database session.
    FastAPI will use this to inject database sessions into route handlers.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()