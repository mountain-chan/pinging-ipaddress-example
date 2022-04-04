import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import pytz

from enums import RECIPIENTS, SENDER_EMAIL


class MyMail:
    def __init__(self, ipaddress, server_status="DOWN"):
        self.port = 465
        self.smtp_server = "smtp.gmail.com"
        self.mail_username = SENDER_EMAIL
        self.mail_password = "<your_mail_password>"  # paste your app password if your account have 2-Step Verification
        self.sender_email = SENDER_EMAIL
        self.ipaddress = ipaddress

        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = "STATUS SERVER: " + ipaddress
        self.message["From"] = self.sender_email
        self.message["To"] = ", ".join(RECIPIENTS)

        self.my_dt = datetime.now(tz=pytz.timezone("Asia/Ho_Chi_Minh")).strftime("%d-%m-%Y %H:%M:%S")

        self.html = "<html> <body> " \
                    "<h4>YOUR SERVER IS " + server_status + "</h4> " \
                    "<p><strong>Time: " + self.my_dt + "</strong></p>" \
                    "<p>Wish you have a pleasant working day!</p> " \
                    "</body> </html> "

        self.html = MIMEText(self.html, "html")
        self.message.attach(self.html)

    def send_mail(self):
        try:
            with smtplib.SMTP_SSL(host=self.smtp_server, port=self.port) as server:
                server.connect(host=self.smtp_server, port=self.port)
                server.login(self.mail_username, self.mail_password)
                server.sendmail(self.sender_email, RECIPIENTS, self.message.as_string())
            print("Successfully sent email!")
        except smtplib.SMTPException as ex:
            print(f"SEND EMAIL ERROR: {str(ex)}")
