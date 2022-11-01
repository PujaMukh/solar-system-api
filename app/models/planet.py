from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    diameter = db.Column(db.Integer)
    gravity = db.Column(db.Float)
    color = db.Column(db.String)
    has_moon = db.Column(db.Boolean)