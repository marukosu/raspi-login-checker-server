from server import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), index=True, nullable=False, unique=True)
    cards = db.relationship('Card', backref='user', lazy=True)

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return f'<User {self.username}>'