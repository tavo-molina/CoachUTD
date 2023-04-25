from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # set up login with flask-login
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from .models import User

    login_manager.user_loader(lambda user_id: User.query.get(int(user_id)))

    # register controllers
    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    from .profile import profile as profile_blueprint

    app.register_blueprint(profile_blueprint)

    from .onboarding import onboarding as onboarding_blueprint

    app.register_blueprint(onboarding_blueprint)

    return app