
from flask import Blueprint, redirect,render_template, request,url_for,flash,send_file
from .models import User,News
from werkzeug.security import check_password_hash, generate_password_hash
from . import db
from flask_login import login_user ,login_required ,logout_user
from werkzeug.utils import secure_filename
import os
from datetime import date,datetime



auth = Blueprint('auth',__name__)



@auth.route('/login',methods=['GET','POST'])
def login():
    admin = User.query.filter_by(username="admin").first()
    if not admin:
        admin=User(username="admin",password=generate_password_hash('123',method='sha256'))
        db.session.add(admin)
        db.session.commit() 
    if request.method == 'POST':
        username=request.form.get('username')
        password=request.form.get('password')
        admin = User.query.filter_by(username=username).first()
        if admin:
            if check_password_hash(admin.password,password):
                login_user(admin,remember=True)
                return redirect(url_for('auth.admin'))
            else :
                return redirect(url_for('auth.login'))

        else :
              return redirect(url_for('auth.login'))
    else:
        return render_template("login.html")

        

@auth.route('/logout',methods={'GET','POST'})
def logout():
    logout_user()
    return redirect(url_for('auth.login'))



@auth.route('/signup')
def signup():
        return "<h1>comming soon</h1>"





@auth.route('/admin',methods=['GET','POST'])
@login_required
def admin():        
    all_data = News.query.all()
 
    if request.method == 'POST':

        if request.form['submit'] == 'logout':
            return redirect(url_for('auth.logout'))

        else:
            return render_template("admin.html", news = all_data)
    else :
        return render_template("admin.html", news = all_data)






@auth.route('/insert', methods = ['GET', 'POST'])
def insert():
 
    if request.method == 'POST':
 
        title = request.form['title']
        description = request.form['description']            
        file = request.files['file'] 
        date=datetime.strptime(request.form['date'],'%Y-%m-%d')
        my_data = News(title=title, paragraph=description,picture=file.read(),picture_name=file.filename,date=date)
        db.session.add(my_data)
        db.session.commit()
        flash("Inserted Successfully")
 
    return redirect(url_for('auth.admin'))





@auth.route('/update', methods = ['GET', 'POST'])
def update():
 
    if request.method == 'POST':
        my_data = News.query.get(request.form.get('id'))
 
        my_data.title = request.form['title']
        my_data.paragraph = request.form['description']
        if request.form['date'] == '':
            my_data.date = datetime.now()
        else:
            my_data.date = datetime.strptime(request.form['date'],'%Y-%m-%d')
        picture=request.files['file']
        my_data.picture = picture.read()
        my_data.picture_name = picture.filename



 
        db.session.commit()
        flash("Updated Successfully")

    return redirect(url_for('auth.admin'))






@auth.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = News.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Deleted Successfully")
 
    return redirect(url_for('auth.admin'))
