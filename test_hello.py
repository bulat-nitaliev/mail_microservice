import aio_pika
import asyncio

async def hello():
    connection = await aio_pika.connect_robust()
    channel = await connection.channel()
    await channel.declare_queue(name='hello')
    message =  aio_pika.Message(body='Hello world'.encode())
    await channel.default_exchange.publish(
        message=message,
        routing_key='hello'
        )
    await connection.close()


if __name__ == '__main__':
    asyncio.run(hello())