from flask import Flask
from .extensions import db
from .controllers.media_controller import bp as media_bp
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(media_bp)

    with app.app_context():
        db.create_all()

    return app
