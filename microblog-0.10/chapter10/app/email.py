import logging
from threading import Thread
from flask import render_template
from flask_mail import Message
from app import app, mail

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_async_email(app, msg):
    with app.app_context():
        try:
            logger.info("Sending email to %s", msg.recipients)
            mail.send(msg)
            logger.info("Email sent successfully")
        except Exception as e:
            logger.error("Failed to send email: %s", str(e))

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    logger.info("Preparing to send email with subject: %s", subject)
    Thread(target=send_async_email, args=(app, msg)).start()

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt', user=user, token=token),
               html_body=render_template('email/reset_password.html', user=user, token=token))
