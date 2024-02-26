from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# pythonanywhereでデプロイする場合のmysql
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://randaction:2024-spring-hackathon-group2@randaction.mysql.pythonanywhere-services.com/randaction$randaction' 

#ローカル環境でテストする場合のmysql
# 0. mysqlをダウンロードする。Macユーザーでhomebrew使っているならHomeberwでダウンロードしてパスを通す
# pip install requirements.txtをしてrequirements.txtにあるライブラリを全てダウンロードする
# 1. randaction という名前のdatabaseを作る(CREATE DATABASEコマンド)
# 2. create_db.pyを実行する

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/randaction' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from .routes import *