# Create the database

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

SQLALCHEMY_DATABASE_URL = "postgresql://beatriz:password123@localhost/mini_project_learning"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency function for FastAPI
def get_db():
    db: Session = SessionLocal()   # create a new DB session
    try:
        yield db                  # yield it to the endpoint
    finally:
        db.close()                # close the session after the request