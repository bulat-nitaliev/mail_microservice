from dataclasses import dataclass
from config import Settings
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl


@dataclass
class MailClient:
    settings: Settings


    def send_message(self,subject:str, text:str, to:str):
        msg = self.build_message(subject=subject,text=text, to=to)
        self.send_msg(msg=msg)



        
    def build_message(self,subject:str,text:str,to)->MIMEMultipart:
        msg = MIMEMultipart()

        msg['From'] = self.settings.EMAIL_HOST_USER
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(_text=text))

        return msg


    def send_msg(self,msg:str):
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL(host=self.settings.EMAIL_HOST, port=self.settings.EMAIL_PORT, context=context)
        server.login(user=self.settings.EMAIL_HOST_USER, password=self.settings.EMAIL_HOST_PASSWORD)
        server.send_message(msg=msg)
        server.quit()