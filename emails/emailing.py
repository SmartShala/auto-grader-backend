import smtplib,ssl
import json
from django.template.loader import render_to_string
from auto_grader.env import credentials
import traceback


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
        #for emails that use ssl
        if self.EMAIL_USE_SSL:
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

        #if the body passed is as html file path
        if istemplate:
            body = render_to_string(body,context) #converted to plain text
        #putting details into the message format
        self.MESSAGE = self.MESSAGE.format(self.SENDER_EMAIL, receiver, sub, body)
        
        try:
            server.sendmail(self.SENDER_EMAIL, receiver, self.MESSAGE)
            self.close_connection(server)
        except Exception as e:
            traceback.print_exc()
            print('Error Sending Email:%s'%str(e))
            return str(e)
            

class titanEmailHandler(EmailHandler):
    EMAIL_HOST = credentials.get('email',{}).get('host')

