from . import db



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = true)
    username = db.Column(db.string(255))

    def __repr__(self):
        return f'User {self.username}'
