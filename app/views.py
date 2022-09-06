
from flask import Blueprint,render_template,url_for,request,redirect
from . import db
from .models import User,Blog,Comment
from flask_login import login_user, login_required, logout_user, current_user,login_manager

views = Blueprint('views', __name__)

@views.route('/home')
@login_required
def home():
    return render_template('home.html',blogs=Blog.query.filter_by().all())

@views.route('/blog/<string:id>',methods=["GET","POST"])
@login_required
def blog(id):
    if request.method =="GET":
        return render_template("content.html",blog =Blog.query.filter_by(blog_id =id).first(),user=current_user,comments=Comment.query.filter_by(blog_id=id).all())
    else:
        db.session.add(Comment(blog_id=id,comment_content=request.form["textarea1"],user_id=current_user.id))
        db.session.commit()

@views.route('/login',methods=["GET","POST"])
def login():
    if request.method =="GET":
        return render_template("login.html")
    else:
        email = request.form["email"]
        password =request.form["password"]
        print(email,password)
        if User.query.filter_by(email=email,password=password).first():
        
            user=User.query.filter_by(email=email,password=password).first()
            login_user(user, remember=True)
        
            return render_template("home.html",blogs=Blog.query.filter_by().all())
        else:
            return ""
@views.route('/password')
def password():
    return render_template("password.html")

