from django.contrib import admin
from .models import Mailing, Client, Message


# Register your models here.

class MailingAdmin(admin.ModelAdmin):
    list_display = ()
