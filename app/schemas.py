# Define how data enters and leaves:
# - validate incoming requests
# - control what data is returned
# - convert SQLAlchemy to JSON safely

from pydantic import BaseModel

# ensure email and name exist and are strings
class UserCreate(BaseModel):
    email: str
    name: str

class UserUpdate(BaseModel):
    name: str

class UserResponse(BaseModel):
    id: int
    email: str
    name: str

    # Tell Pydantic how to build a schema from SQLAlchemy model
    # Needed because FastAPI endpoints often return SQLAlchemy objects (which aren't JSON)
    class Config:
        from_attributes = True #This schema can be created from an object that has attributes, not just from a dict (Pydantic expects a dict)
        # SQLAlchemy object  →  Pydantic schema  →  JSON
        # there is no Config class in the other classes (UserUpdate and UserCreate) because they are inputs,
        # (while UserResponse is output) and already a dict-like JSON, so there is no SQLAlchemy involved.