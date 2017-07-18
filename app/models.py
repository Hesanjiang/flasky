from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Colunmn(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForgignKey('roles.id'))


