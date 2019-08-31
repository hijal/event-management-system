from django.contrib import admin

from .models import Location, City, Place, Center


admin.site.register(Location)
admin.site.register(City)
admin.site.register(Place)
admin.site.register(Center)