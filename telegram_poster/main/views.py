from django.shortcuts import render
from .models import Client, TelegramUser
from telegram_poster.settings import TELEGRAM_ID, TELEGRAM_KEY, TELEGRAM_SESSION_NAME
# Create your views here.
import asyncio
from telethon import TelegramClient
from telegram_poster.tasks import send_message
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request,'index.html')

@csrf_exempt
def notify(request):

    print(request.POST['secret'])
    
    
    try:
        c = Client.objects.get(secret=request.POST['secret'])
        for user in TelegramUser.objects.filter(client=c):
            print(user)
            message = request.POST['message']+' Источник: '+c.name
            send_message.delay(user.key,request.POST['message'])
            
    except:
        pass
    #loop.close()

    if request.method == 'POST':
        print('post')
    return render(request,'index.html')