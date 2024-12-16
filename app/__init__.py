import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from app.routes.user_routes import user_routes
from app.routes.main_routes import main_routes

# Load env variables from .env
load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')  # Get from .env
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    migrate.init_app(app, db)  # Bind flask-migrate to the app and SQLAlchemy
    
    # Register Blueprints
    app.register_blueprint(main_routes)
    app.register_blueprint(user_routes)

    # Import models here to make sure they are loaded
    from app.models.user import User

    return app

