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
class Pet(db.Model):
    __tablename__='pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
