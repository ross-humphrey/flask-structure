# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
# from flask.ext.sqlalchemy import SQLAlchemy

from flask_sqlalchemy import SQLAlchemy

# Define the database object which is imported
# by modules and controllers


def create_app():
    # Define the WSGI application object
    app = Flask(__name__)

    # Configurations
    app.config.from_object('config')

    # # Define the database object which is imported
    # # by modules and controllers
    # db = SQLAlchemy(services)

    # Sample HTTP error handling
    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    # Import a module / component using its blueprint handler variable (mod_auth)
    from mod_auth.controllers import mod_auth as auth_module

    # Register blueprint(s)
    app.register_blueprint(auth_module)
    # services.register_blueprint(xyz_module)
# ..

    return app


app = create_app()
db = SQLAlchemy(app)
db.create_all()

