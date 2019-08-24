import os
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app
from flask_login import UserMixin

from app.extensions import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password_hash = db.Column(db.String(128))
    auth = db.Column(db.Integer, default=0)

    files = db.relationship('File', cascade='all')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(256))
    hash_name = db.Column(db.String(80))
    upload_date = db.Column(db.DateTime, default=datetime.now)
    file_size = db.Column(db.Integer)
    remark = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    user = db.relationship('User')
    category = db.relationship('Category')

    def get_size(self):
        file_size = self.file_size
        units = ['B', 'K', 'M', 'G']
        for unit in units:
            if file_size >= 1024:
                file_size /= 1024
            else:
                return "{:.1f} {}".format(file_size, unit)



class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    level = db.Column(db.Integer)
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    parent = db.relationship('Category', back_populates='subs', remote_side=[id])
    subs = db.relationship('Category', back_populates='parent', cascade='all')
    files = db.relationship('File', cascade='all')


@db.event.listens_for(File, 'after_delete', named=True)
def delete_file(**kwargs):
    target = kwargs['target']
    if os.path.exists(os.path.join(current_app.config['UPLOAD_PATH'], target.hash_name)):
        os.remove(os.path.join(current_app.config['UPLOAD_PATH'], target.hash_name))
