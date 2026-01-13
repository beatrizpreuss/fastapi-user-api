# Create the tables in the database (defined in database.py) for each model (defined in models.py)

from .database import Base, engine
from .models import User #this is enough to put the User model inside the Base.metadata

# This creates all tables in the database defined in database.py
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")