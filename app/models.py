from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin

class Blog(db.Model):
    blog_id = db.Column(db.Integer,primary_key =True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    blog_title = db.Column(db.String(25))
    blog_content = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime(timezone=True), default=func.now())


    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key =True)
    email = db.Column(db.String(25),unique = True)
    name = db.Column(db.String(25))
    password = db.Column(db.String(25))

class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer,db.ForeignKey('blog.blog_id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    comment_content = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime(timezone=True), default=func.now())

