from telegram_poster.celery import app
from celery import shared_task 
from telegram_poster.settings import TELEGRAM_ID, TELEGRAM_KEY, TELEGRAM_SESSION_NAME
import asyncio
from telethon import TelegramClient
from main.models import TelegramUser

async def send(phone,client,message):
    print('Send test ')
    await client.connect()
    await client.send_message(phone, message) 
    #await client.send_message('+380509123925', 'test') 
    #await client.send_message('+380507750630', 'test') 

@shared_task
def send_message(phone,message):
    print('Sending message')
    #user = TelegramUser.objects.get(pk=user_id)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    client = TelegramClient(TELEGRAM_SESSION_NAME,TELEGRAM_ID,TELEGRAM_KEY,loop=loop)
    loop.run_until_complete(send(phone,client,message))