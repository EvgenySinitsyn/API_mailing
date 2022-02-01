from django.contrib import admin
from .models import Mailing, Client, Message


# Register your models here.

class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_begin', 'text', 'properties_of_clients', 'time_end')
    search_fields = ('id', 'text', 'properties_of_clients')
    list_editable = ('time_begin', 'text', 'properties_of_clients', 'time_end')
    list_filter = ('time_begin', 'text', 'properties_of_clients', 'time_end')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'tel_num', 'operator_code', 'tag', 'timezone')
    search_fields = ('id', 'tel_num', 'operator_code', 'tag', 'timezone')
    list_editable = ('tel_num', 'operator_code', 'tag', 'timezone')
    list_filter = ('tel_num', 'operator_code', 'tag', 'timezone')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'createsendtime', 'sent', 'mailing_id', 'client_id')
    search_fields = ('id', 'createsendtime', 'sent', 'mailing_id', 'client_id')
    list_editable = ('sent',)
    list_filter = ('createsendtime', 'sent', 'mailing_id', 'client_id')

admin.site.register(Mailing, MailingAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Message, MessageAdmin)