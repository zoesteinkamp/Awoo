from django.contrib import admin
from .models import User,Dating,Hobby,HobbyPerson,Message

admin.site.register(User)
admin.site.register(Dating)
admin.site.register(Hobby)
admin.site.register(HobbyPerson)
admin.site.register(Message)
