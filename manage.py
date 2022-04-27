from flask.cli import FlaskGroup
from flask_sqlalchemy import SQLAlchemy

from app import app

cli = FlaskGroup(create_app=app)
# Define the database object which is imported
# by modules and controllers


if __name__ == '__main__':
    # Local server - without docker
    app.run(host='0.0.0.0', port=8080, debug=True)
