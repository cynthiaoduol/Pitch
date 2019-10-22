from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__ ='users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref='user',lazy='dynamic')
    pass_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_hash = generate_password_hash(password)

    def verify_password(self,password)
        return check_password_hash(self.pass_hash,password)

    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):
    __tablename__='pitches'
    id = db.Column(db.Integer,primary_key = True)
    pitch_category = db.Column(db.String(255))
    pitch_text = db.Column(db.String())
    user_id = db.column(db.Integer,db.ForeignKey('users_id'))

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    


