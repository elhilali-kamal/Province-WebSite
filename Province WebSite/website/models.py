from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin
from datetime import date



class News(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    date=db.Column(db.Date,default=func.now())
    paragraph=db.Column(db.String(5000))
    picture_name=db.Column(db.String(500))
    picture=db.Column(db.BLOB)


class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    password=db.Column(db.String(100))
    
