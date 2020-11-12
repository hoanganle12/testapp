from flask import Flask
from flask import app
from flask_sqlalchemy import  SQLAlchemy
from flask_admin import Admin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pysql://root:123456@localhost/saledby1?charset =utf8'
app.config['SQlAlCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app=app)

admin = Admin(app=app, name="Testname", template_mode="bootstrap4")