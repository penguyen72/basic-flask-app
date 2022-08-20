from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # This encrypts the cookies and session data related to website
    app.config["SECRET_KEY"] = 'super_secret_key'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth, url_prefix = "/")

    return app