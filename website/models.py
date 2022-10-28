from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    team=db.Column(db.String(150), unique=True)
    password=db.Column(db.String(150))
    country=db.Column(db.String(150))
    # add a relationship to thePlayers model
    notes = db.relationship('Players')
class Players(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    data=db.Column(db.String(10000))
    date=db.Column(db.DateTime(timezone=True),default=func.now()) 
    # add a relationship to the User model
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
# Path: website/views.py