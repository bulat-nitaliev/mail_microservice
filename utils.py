
import json
from aiokafka import AIOKafkaConsumer
from config import Settings
from service import MailService
from client import MailClient


consumer = AIOKafkaConsumer(
    'email_topic',
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda message: json.loads(message.decode('utf-8'))
)

async def get_mail_service()->MailService:
    return MailService(
        mail_client=MailClient(settings=Settings())
    )


async def consume_message():
    mail_service = await get_mail_service()
    await consumer.start()
    try:
        async for mg in consumer:
            print(mg)
            await mail_service.consume_mail(message=mg)
    finally:
        await consumer.stop()

# async def make_consumer(settings:Settings):
#     mail_service = await get_mail_service()
#     connection = await aio_pika.connect(url=settings.BROKER_URL)
    
#     async with connection:
#         channel = await connection.channel()
        
#         name ='email_queue'
#         queue = await channel.declare_queue(name=name, durable=True)
        
        
#         await queue.consume(mail_service.consume_mail)
        
