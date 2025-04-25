from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configurations if any
    # app.config.from_object('config.Config')

    # Register blueprints if using
    # from .routes import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    return app