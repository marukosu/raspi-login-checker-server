from datetime import datetime

from server import db


class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    idm = db.Column(db.String(16), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, idm):
        self.idm = idm

    def __repr__(self):
        return f'<Card user_id:{self.user_id} idm:{self.idm}>'
