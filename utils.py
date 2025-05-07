
import aio_pika
from config import Settings
from service import MailService
from client import MailClient


async def get_mail_service()->MailService:
    return MailService(
        mail_client=MailClient(settings=Settings())
    )

async def make_consumer(settings:Settings):
    mail_service = await get_mail_service()
    connection = await aio_pika.connect_robust(url=settings.BROKER_URL)
    
    async with connection:
        channel = await connection.channel()
        
        name ='email_queue'
        queue = await channel.declare_queue(name=name, durable=True)
        
        
        await queue.consume(mail_service.consume_mail)
