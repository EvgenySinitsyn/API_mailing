from django.db import models

# Create your models here.

class Mailing(models.Model):
    time_begin = models.DateTimeField()
    text = models.CharField(max_length=300)
    properties_of_clients = models.CharField(max_length=100)
    time_end = models.DateTimeField()

    def __str__(self):
        return self.text

class Client(models.Model):
    tel_num = models.BigIntegerField(max_length=11)
    operator_code = models.IntegerField(max_length=4)
    tag = models.CharField(max_length=100)
    timezone = models.CharField(max_length=10)

    def __str__(self):
        return self.tag

class Message(models.Model):
    createsendtime = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(default=False)
    mailing_id = models.ForeignKey('Mailing', on_delete=models.CASCADE)
    client_id = models.ForeignKey('Client', on_delete=models.CASCADE)

    def __str__(self):
        return self.createsendtime

