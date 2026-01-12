from .database import Base, engine
from .models import User

# This creates all tables in the database defined in database.py
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")