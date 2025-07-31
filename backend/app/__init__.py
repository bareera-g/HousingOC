from flask import Flask
from .routes import listings, eligibility, waitlists, roommates

def create_app():
    app = Flask(__name__)
    
    # Register Blueprints
    app.register_blueprint(listings.bp)
    app.register_blueprint(eligibility.bp)
    app.register_blueprint(waitlists.bp)
    app.register_blueprint(roommates.bp)

    return app
