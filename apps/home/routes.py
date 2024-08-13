from flask import jsonify

from apps import db
from apps.home import blueprint
from apps.llm.llm_provider import ChatLLM
from apps.models import Chats

chat = ChatLLM(model='llama3')


@blueprint.route('/')
def index():
    # chat_record = Chats(title='Om')
    # db.session.add(chat_record)
    # db.session.commit()
    return chat.get_title('National Bird', 'Peacock'), 201
