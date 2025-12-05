from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///myDatabase.db' 
app.config['SECRET_KEY'] = '48acc0b5273209690ee832e5'
db=SQLAlchemy(app)
migrate = Migrate(app,db)

from .models import *
from .routers import *
