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
    def send_mail(self, message: str)->None:
        """_Create an SMTP object, login with gmail credentials, send mail and close connection_

        Args:
            message (str): _Chosen Birthday wish_
        >>>Example
            send_mail_object.send_mail('Hello John, Happy Birthday')
        """
        connection = SMTP(host= self.host)
        connection.starttls()
        connection.login(user= self.email, password= self.password)
        connection.sendmail(from_addr= self.email, to_addrs= self.receiver_email , msg= message)
        connection.close()
    def get_details(self)->None:
        """_Read the env file and gets the email credentials_
        """
        self.email = os.getenv("GMAIL_ACC")
        self.password = os.getenv("GMAIL_APP_PASSWORD")
        self.receiver_email = os.getenv("RECEIVER_EMAIL")