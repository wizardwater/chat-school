from flask import Blueprint, render_template, request, jsonify, redirect, session
from flask_socketio import emit
from datetime import datetime
from .. import conn, socketio  # 여기서는 모듈 간의 의존성을 최소화합니다.

bp = Blueprint('chatbot', __name__, url_prefix='/edu_chatbot')


@bp.route('/')
def show_chatbot_page():
    return render_template('./Student_page/Chatbot_choice_page/chatbot_choice_page.html')

@bp.route('/submit_doc_to_chatbot')
def submit_doc_to_chatbot():
    return render_template('Student_page/Chatbot_Or_Communication_Page/Chatbot_or_communication_page.html')
@socketio.on('connect', namespace='/chatbot')
def connect():
    print('Client chatbot connected')
    uid="082d8640-9287-4284-9a73-47543b255309"
    if 'user' in session:
        uid = session['user']['uid']
    else:
        print('User not found in session')
    
    
    data=conn.tb_select('Chat','학생_ID',uid)
    print(data)
    emit('chatting',data)