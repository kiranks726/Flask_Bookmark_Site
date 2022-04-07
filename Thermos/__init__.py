import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment

app=Flask(__name__)

basedir=os.path.abspath(os.path.dirname(__file__))

# Configure database
app.config['SECRET_KEY']=b'\xb4\xc07\xd4n\xb0`-i \xc3\xb0 f\x16\xa4\x0f\xb0\xff\x87\xa6\xd5\xd3y'
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///" + os.path.join(basedir,'Thermos.db')
db=SQLAlchemy(app)

# configure authentication
login_manager=LoginManager()
login_manager.session_protection="strong"
login_manager.login_view="login"
login_manager.init_app(app)


moment=Moment(app)

import Thermos.Models
import Thermos.views
