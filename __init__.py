from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///idlegame.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy for database
db = SQLAlchemy(app)

# Resources, Generators, Other Models Here:
# class Resources(db.Model):


# Columns and relationships


# Import and register Blueprints

from .resources import resources
app.register_blueprint(resources)


# from .generators import generators
#
# app.register_blueprint(generators)


# Initialize future blueprints for prestiges, analytics, etc


@app.route('/')
def home():
    db.create_all()
    return {"message": "Welcome to Idle Game API!"}


if __name__ == '__main__':
    # Create DB if not exists
    with app.app_context():
        db.create_all()

    app.run()