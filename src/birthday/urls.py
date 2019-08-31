from django.urls import path
from .views import (
        selection, 
        eventtype, 
        guest_number,
        select_date,
        selection_detail
    )
urlpatterns = [
    path('select/', selection, name = 'select'),
    path('types/', eventtype, name = 'eventtype'),
    path('guests/', guest_number, name = 'guest'),
    path('date/', select_date, name = 'date'),
    path('detail/', selection_detail, name = 'detail'),
]
