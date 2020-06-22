from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    secret = models.CharField(max_length=250, db_index=True)

class TelegramUser(models.Model):
    key = models.CharField(max_length=250, db_index=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)