from apps import db
from datetime import datetime


class Chats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Define the one-to-many relationship with ChatHistory
    chat_histories = db.relationship('ChatHistory', backref='chat', lazy=True)

    def __repr__(self):
        return f'<Chat {self.title}>'


class ChatHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chats.id'), nullable=False)
    user_prompt = db.Column(db.Text, nullable=False)
    ai_response = db.Column(db.Text, nullable=False)
    embeddings = db.Column(db.PickleType, nullable=True)  # or use another type if more suitable
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<ChatHistory {self.id}>'
