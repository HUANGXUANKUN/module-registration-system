from __init__ import db


class Users(db.Model):
    uname = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.uname


class Student(db.Model):
    uname = db.Column(db.String, primary_key=True)
    matric_no = db.Column(db.String, nullable=False)
    bid_point = db.Column(db.Integer, nullable=False)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.uname


class Admin(db.Model):
    uname = db.Column(db.String, primary_key=True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.uname
