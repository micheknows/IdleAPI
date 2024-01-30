# models.py
from . import db
from flask_sqlalchemy import SQLAlchemy



class ResourceModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    icon_url = db.Column(db.String(2048))
    description = db.Column(db.Text())

    amount = db.Column(db.Integer(), default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "icon_url": self.icon_url,
            "description": self.description,
            "amount": self.amount
        }

    def __repr__(self):
        return f"<Resource {self.name}>"