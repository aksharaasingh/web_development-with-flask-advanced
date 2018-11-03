from app import db,bcrypt
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    user_name = db.Column(db.String(80))
    user_email = db.Column(db.String(30),unique = True,index = True)
    user_password = db.Column(db.String(30))
    registration_date = db.Column(db.DateTime, default=datetime.utcnow())

    @classmethod
    def create_user(cls,user,email,password):
        user = cls(user_name = user,
                   user_email = email,
                   user_password = bcrypt.generate_password_hash(password))

        db.session.add(user)
        db.session.commit()
        return user
