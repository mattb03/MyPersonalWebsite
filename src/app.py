from flask import Flask, request, flash, redirect
from wtforms import Form, StringField, validators
from database import db_session, init_db
from models import Message

app = Flask(__name__)

app.secret_key = 'very-secret-key'

class ContactForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.Length(min=1, max=50)])
    message = StringField('Message', [validators.Length(min=1, max=250)])

@app.route('/sendMessage', methods=['POST'])
def send_message():
    form = ContactForm(request.form)
    if form.validate():
        message = Message(form.name.data, form.email.data, form.message.data)
        db_session.add(message)
        flash('Thanks for your message!')
    else:
        flash('There was an error sending me your message')

    return redirect('http://localhost:8080/#ContactSection')
    
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    print ('initializing db')
    init_db()
    print ('********** current database ************')
    Message.query.all()