from smtplib import SMTP
from dotenv import load_dotenv
import os
class SendMail:
    def __init__(self):
        self.host = "smtp.gmail.com"
        self.password = ""
        self.email = ""
        self.receiver_email = ""
        load_dotenv(dotenv_path="./data.env")
        self.get_details()
    def send_mail(self, message: str):
        connection = SMTP(host= self.host)
        connection.starttls()
        connection.connect()
        connection.login(user= self.email, password= self.password)
        connection.sendmail(from_addr= self.email, to_addrs= self.receiver_email , message= message)
        connection.close()
    def get_details(self):
        self.email = os.getenv("GMAIL_ACC")
        self.password = os.getenv("GMAIL_APP_PASSWORD")
        self.receiver_email = os.getenv("RECEIVER_EMAIL")