import pyotp
from emailing import titanEmailHandler
import json
from base64 import b32encode

class OtpMail(titanEmailHandler):
    with open(".env.json", 'r') as fp:
        data = json.loads(fp.read())["email"]["otp"]
        mail = data["mail"]
        password = data["pass"]
    
    SENDER_EMAIL = mail
    SENDER_PASSWORD = password

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


if __name__ == '__main__':
    x = OtpHandler()
    m = "royimonroy@gmail.com"
    otp = x.generation(m)
    form = '''<div style="font-family: Helvetica,Arial,sans-serif;min-width:1000px;overflow:auto;line-height:2">
    <div style="margin:50px auto;width:70%;padding:20px 0">
    <div style="border-bottom:1px solid #eee">
      <a href="" style="font-size:1.4em;color: #00466a;text-decoration:none;font-weight:600">Your Brand</a>
    </div>
    <p style="font-size:1.1em">Hi,</p>
    <p>Thank you for choosing SmartShala. Use the following OTP to complete your Sign Up procedures. OTP is valid for 10 minutes</p>
    <h2 style="background: #00466a;margin: 0 auto;width: max-content;padding: 0 10px;color: #fff;border-radius: 4px;">{}</h2>
    <p style="font-size:0.9em;">Regards,<br />SmartShala</p>
    <hr style="border:none;border-top:1px solid #eee" />
    <div style="float:right;padding:8px 0;color:#aaa;font-size:0.8em;line-height:1;font-weight:300">
      <p>SmartShala</p>
      <p>Smart India Hackathon</p>
      <p>India</p>
    </div>
  </div>
</div>'''
    x.send_mail(m,form.format(otp), "OTP")
