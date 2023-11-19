from flask import Flask
from flask_smorest import Api

from db import db
from resources.athlete import blp as AthleteBlueprint
from resources.event import blp as EventBlueprint
from resources.result import blp as ResultBlueprint

# Factory pattern
def create_app():
    app = Flask(__name__)
    
    # Config
    app.config["DEBUG"] = True
    app.config["API_TITLE"] = "Flask workshop REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.1.0"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db" 
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # Initialize database
    db.init_app(app)
    
    # Create database tables
    with app.app_context():
        db.create_all()
        
    # Build API
    api = Api(app)
    api.register_blueprint(AthleteBlueprint)
    api.register_blueprint(EventBlueprint)
    api.register_blueprint(ResultBlueprint)
    
    return app