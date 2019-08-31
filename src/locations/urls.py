from django.urls import path
from .views import check, load_cities, load_com_center

urlpatterns = [
    path('event/', check, name='check'),
    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),
    path('ajax/load-center/', load_com_center, name='ajax_load_center'),
]
