# server/app.py

#  Imports the Flask class, which is used to create the main web application object (app).
from flask import Flask
# Imports the Migrate class from Flask-Migrate, which helps manage database migrations (e.g., creating, altering tables over time).
from flask_migrate import Migrate

# Imports the db object (an instance of SQLAlchemy) from your models.py file, which is used to define your database models and interact with the database.
from models import db

# Creates the Flask application instance, which is the central object of your web app.
# __name__ tells Flask where to find resources related to this module.
app = Flask(__name__)

# Tells SQLAlchemy how to connect to the database.
# Here, you're using SQLite, and the database will be stored in a file called app.db in the current directory.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Disables a feature that tracks object changes in memory, which you don’t need unless you're building something very advanced.
# Setting this to False saves memory and avoids a warning.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creates a Migrate object, connecting your Flask app and database.
# This sets up Flask-Migrate so you can use commands like flask db migrate and flask db upgrade to manage schema changes.
migrate = Migrate(app, db)

# Initializes the SQLAlchemy db object with the Flask app, linking the database models and config to the Flask app environment.
db.init_app(app)

# This block ensures the app only runs when the script is executed directly.
# app.run(...) starts the Flask development server.
# port=5555 sets the server to run on port 5555.
# debug=True enables debug mode:
# Reloads the server when you make code changes
# Shows detailed error messages in the browser
if __name__ == '__main__':
    app.run(port=5555, debug=True)
