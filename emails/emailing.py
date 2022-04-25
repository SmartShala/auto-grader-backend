import smtplib,ssl
import json
from django.template.loader import render_to_string

class EmailHandler:
    SENDER_EMAIL = ''
    SENDER_PASSWORD =''
    EMAIL_PORT = 465
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_USE_SSL = True
    MESSAGE = """From: {}
To: {}
MIME-Version: 1.0
Content-type: text/html
Subject: {}



{}
"""

    def open_connection(self):
        if self.EMAIL_USE_SSL:
            # Create a secure SSL context
            context = ssl.create_default_context()
            server = smtplib.SMTP_SSL(self.EMAIL_HOST, self.EMAIL_PORT, context=context)

        else:
            server = smtplib.SMTP(self.EMAIL_HOST, self.EMAIL_PORT)
        return server

    def close_connection(self, server):
        server.quit()

    def send_mail(self, receiver, body='', sub='', istemplate=False, context={}):
        server = self.open_connection()
        server.login(self.SENDER_EMAIL, self.SENDER_PASSWORD)
        if istemplate:
            body = render_to_string(body,context)
        self.MESSAGE = self.MESSAGE.format(self.SENDER_EMAIL, receiver, sub, body)
        try:
            server.sendmail(self.SENDER_EMAIL, receiver, self.MESSAGE)
        except Exception as e:
            return e
        finally:
            self.close_connection(server)

class titanEmailHandler(EmailHandler):
    with open(".env.json", 'r') as fp:
        host = json.loads(fp.read())['email']['host']
    EMAIL_HOST = host

