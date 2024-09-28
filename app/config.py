# app/config.py

import os

# Set the base directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Configuration for the Flask application
class Config:
    # Secret key for session management and CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "storyweaver.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable track modifications for performance
