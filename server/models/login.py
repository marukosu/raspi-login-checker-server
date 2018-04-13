from server import db
from datetime import datetime

class Login(db.Model):
    __tablename__ = 'logins'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())

    def __init__(self, created_at):
        self.created_at = created_at
    
    def __repr__(self):
        return f'<Login user_id:{self.user_id} created_at:{self.created_at}>'