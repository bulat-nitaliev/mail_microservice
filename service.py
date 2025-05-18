from dataclasses import dataclass
from client import MailClient
from aiokafka import AIOKafkaProducer
import json
import asyncio
from schema import EmailBody
from config import Settings


settings = Settings()


event_loop = asyncio.get_event_loop()

producer=AIOKafkaProducer(
            bootstrap_servers='localhost:9092',
            loop=event_loop
        )


@dataclass
class MailService:
    mail_client:MailClient

    async def consume_mail(self,message:dict):
        
            email_body = EmailBody(**message)
            correllation_id = email_body.correllation_id
            try:
                self.send_welcome__email(
                    subject=email_body.subject,
                    text=email_body.message,
                    to=email_body.user_email
                )
            except Exception as e:
                 print('eeeeeee')
                 dt = {'err':str(e), "correllation_id": correllation_id}
                 await self.send_fail_email(dt)

    def send_welcome_email(self, subject, text, to):
        self.mail_client.send_message(
            subject=subject,
            text=text,
            to=to
            )
        
    async def send_fail_email(self,dic:dict )->None:
        await producer.start()
        try:
              await producer.send(
                   'callback_email_topic',
                   value=json.dumps(dic).encode()
              )
        finally:
             await producer.stop()
         
