from flask import Flask
from .controllers.media_controller import bp as media_bp
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.register_blueprint(media_bp)

    return app
