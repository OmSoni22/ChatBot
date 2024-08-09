from flask import jsonify

from apps import db
from apps.home import blueprint
from apps.models import Chats


@blueprint.route('/')
def index():
    chat_record = Chats(title='Om')
    db.session.add(chat_record)
    db.session.commit()
    return jsonify(response='Chat added!'), 201
