# server/models.py

# Imports the SQLAlchemy class from Flask-SQLAlchemy.
# This extension helps you define models (tables) in Python and interact with the database easily.
from flask_sqlalchemy import SQLAlchemy

# Imports the MetaData class from SQLAlchemy.
# This is used to hold details about the structure of your database — such as tables, columns, and constraints.
from sqlalchemy import MetaData

# contains definitions of tables and associated schema constructs
# Creates a metadata object, which stores information about your database schema.
# You’re passing this to SQLAlchemy to keep explicit control of the schema setup.
metadata = MetaData()

# create the Flask SQLAlchemy extension
# Creates a db object, which is your SQLAlchemy instance configured to use the custom metadata.
# You’ll use this db object to:
# Define models (db.Model)
# Create tables
# Run queries
db = SQLAlchemy(metadata=metadata)

# define a model class by inheriting from db.Model.
# Defines a model class named Pet, which will represent the pets table in the database.
# It inherits from db.Model, so SQLAlchemy knows to treat this as a table.
class Pet(db.Model):

    #  Explicitly sets the name of the table in the database as "pets".
    # If you didn’t include this, SQLAlchemy would default to using "pet" (the class name, lowercase).
    __tablename__ = 'pets'

    # Defines the following:
    # A column named id, of type Integer, and marks it as the primary key.
    # This uniquely identifies each pet.
    id = db.Column(db.Integer, primary_key=True)

    # A column named name, of type String.
    # This stores the pet's name.
    name = db.Column(db.String)

    # Defines a column named species, also of type String. This stores the type of animal (e.g., dog, cat, etc.).
    species = db.Column(db.String)
