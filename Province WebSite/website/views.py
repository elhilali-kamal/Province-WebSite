from flask import Blueprint ,render_template, request, session
from . import db
from .models import User,News
from werkzeug.security import generate_password_hash


views = Blueprint('views',__name__)


@views.route('/')
def home():
    
    all_data = News.query.all()
    return render_template("index.html", news=all_data )



@views.route('/login')
def login():
    return render_template("login.html")


@views.route('/CONTACT')
def conctact():
    return render_template("contact.html")



@views.route('/index')
def index():
    return render_template("index.html")

    
@views.route('/UNIVERSITE')
def universite():
    return render_template("university.html")


    
@views.route('/FORMATIONS')
def formations():
    return render_template("formation.html")


    
@views.route('/ESPACE')
def espace():
    return render_template("espace.html")


@views.route('/licence')
def licence():
    return render_template("licence.html")


@views.route('/master')
def master():
    return render_template("master.html")


@views.route('/doctorat')
def doctorat():
    return render_template("doctorat.html")



@views.route('/annonce',methods={'GET','POST'})
def annonce():
    if request.method == 'POST':
        result = request.form.get('result')

        return render_template("annonce.html",result =result)
    else:
        return render_template("annonce.html",result="haha")
