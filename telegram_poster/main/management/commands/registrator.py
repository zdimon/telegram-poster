from django.core.management.base import BaseCommand, CommandError
from telethon import TelegramClient, events
from telegram_poster.settings import TELEGRAM_ID, TELEGRAM_KEY, TELEGRAM_SESSION_NAME
import asyncio
from asgiref.sync import sync_to_async, async_to_sync

client = TelegramClient(TELEGRAM_SESSION_NAME,TELEGRAM_ID,TELEGRAM_KEY)

from main.models import Client, TelegramUser

@sync_to_async
def register(message,from_id):
    message = message.lower()
    try:
        c = Client.objects.get(name=message)
        try:
            user = TelegramUser.objects.get(key=from_id)
            message = 'Вы уже зарегистрированы.'
        except:
            u = TelegramUser()
            u.key = from_id
            u.client = c
            u.save()
            message = 'Вы были зарегистрированы.'
    except Exception as e:
        print(e)
        message =  'Запрашиваемый клиент не найден. %s' % e
    return message

@client.on(events.NewMessage())
async def normal_handler(event):
    message = event.message.to_dict()
    print('#%s#' % int(message['from_id']))
    message = await register(message['message'], message['from_id'])
    await client.send_message('+380951237021', message)

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Run registrator')
        client.start()
        client.run_until_disconnected()