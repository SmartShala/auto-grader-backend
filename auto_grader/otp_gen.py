import pyotp
from emails.emailing import titanEmailHandler
import json
from base64 import b32encode
from env import credentials

class OtpMail(titanEmailHandler):
    #getting sender email and password
    email_data = credentials.get('email')
    if email_data is not None:
      mail = email_data.get("mail")
      password = email_data.get("pass")
    
    SENDER_EMAIL = mail
    SENDER_PASSWORD = password

    #overriding the function to add body path
    def send_mail(self, receiver, body='/templates/email/otp_email.html', sub='OTP', 
                  istemplate=True, context={}):
        return super().send_mail(receiver, body, sub, istemplate, context)

class OtpHandler(OtpMail):
    INTERVAL = 600

    def get_secret_key(self, r_mail):
        secret_key = b32encode(r_mail.encode("UTF-8"))
        totp = pyotp.TOTP(secret_key, interval=self.INTERVAL)
        return totp

    def generation(self, r_mail):
        totp = self.get_secret_key(r_mail)
        return totp.now()

    def verification(self, otp, r_mail):
        totp = self.get_secret_key(r_mail)
        return totp.verify(otp)


