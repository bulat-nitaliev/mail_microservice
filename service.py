from dataclasses import dataclass
from client import MailClient
import aio_pika
import json
from schema import EmailBody


@dataclass
class MailService:
    mail_client:MailClient

    async def consume_mail(self,message:aio_pika.abc.AbstractIncomingMessage):
        async with message.process():
            print(message.body.decode())
            email_body = EmailBody(**json.loads(message.body.decode()))
            correllation_id = message.correlation_id
            print(email_body)
            self.send_welcome_email(
                subject=email_body.subject,
                text=email_body.message,
                to=email_body.user_email
            )

    def send_welcome_email(self, subject, text, to):
        self.mail_client.send_message(
            subject=subject,
            text=text,
            to=to
            )
