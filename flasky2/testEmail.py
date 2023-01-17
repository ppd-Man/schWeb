from flask_mail import Message
# from hello import mail
from flask_mail import Mail

msg = Message('test email',sender='it.test@wiidreamthinker.com',recipients=['it.test@wiidreamthinker.com'])
msg.body = 'this is plain text body'
msg.html = 'this is <b>HTML</b> body'
with app.app_context():
    mail.send(msg)
