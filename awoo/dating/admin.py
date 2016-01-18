from django.contrib import admin
from .models import Account,Dating,Hobby,HobbyPerson,Message

admin.site.register(Account)
admin.site.register(Dating)
admin.site.register(Hobby)
admin.site.register(HobbyPerson)
admin.site.register(Message)
