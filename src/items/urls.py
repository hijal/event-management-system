from django.urls import path
from .views import events, event_detail

urlpatterns = [
    path('events/', events, name='events'),
    path('<int:pk>/', event_detail, name='detail'),
]
