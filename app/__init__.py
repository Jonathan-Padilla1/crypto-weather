from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes.user_routes import user_routes
from app.routes.main_routes import main_routes

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(main_routes)
    app.register_blueprint(user_routes)
    return app

