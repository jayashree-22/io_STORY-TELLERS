# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

app = Flask(__name__)

# Load the configuration from config.py
app.config.from_object(Config)

# Initialize the database
db = SQLAlchemy(app)

# Import your routes (important to avoid circular imports)
from app.routes import story_blueprint
app.register_blueprint(story_blueprint)

with app.app_context():
    db.create_all()