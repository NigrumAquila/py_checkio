import sendgrid
from sendgrid.helpers.mail import Email,  Mail, Content

API_KEY = 'Registrate your own API_KEY'
BODY = 'Hi {}'
sg = sendgrid.SendGridAPIClient(API_KEY)

def send_email(email, name):
    from_email = "test@example.com"
	to_email = email
	subject = "Welcome"
	content = Content("text/plain", BODY.format(name))
	mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
