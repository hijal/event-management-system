from django.contrib import admin
from .models import ForWhom, EventType, Guest, HelloDate

admin.site.register(ForWhom)
admin.site.register(EventType)
admin.site.register(Guest)
admin.site.register(HelloDate)