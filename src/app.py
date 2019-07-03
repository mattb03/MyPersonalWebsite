from flask import Flask, request, flash, redirect
from flask_cors import CORS
from wtforms import Form, StringField, validators
from database import db_session, init_db
from models import Message
import json

app = Flask(__name__)
CORS(app)

app.secret_key = 'very-secret-key'

class ContactForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.Length(min=1, max=50)])
    message = StringField('Message', [validators.Length(min=1, max=250)])

@app.route('/sendMessage', methods=['POST'])
def send_message():
    print (request.get_json())
    res = {
        'status_code': 200,
        'message': 'Success'
    }
    return json.dumps(res)
    
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    print ('initializing db')
    init_db()
    print ('********** current database ************')
    Message.query.all()