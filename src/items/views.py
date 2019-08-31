from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Event


def events(request):
    event_list = Event.objects.all()
    args = {
        'event_list': event_list,
    }
    return render(request, 'events/list.html', args)


def event_detail(request, pk=None, *args, **kwargs):
    event_list = Event.objects.get_by_id(pk)
    if event_list is None:
        raise Http404("Event doesn't Exists.")
    args = {
        'event_list': event_list,
    }
    return render(request, 'events/detail.html', args)