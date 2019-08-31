from django.shortcuts import render, redirect
from carts.models import Cart

from .forms import (
        ForWhomForm,
        EventTypeForm, 
        GuestNumberForm,
        DateInputForm,
    )
from .models import (
        ForWhom,
        EventType, 
        Guest,
        HelloDate
    )


def selection(request):
    if request.method == 'POST':
        form = ForWhomForm(request.POST or None)
        if form.is_valid():
            select = request.POST.get('select')
            select = ForWhom(
                select = select,
            )
            select.save()
            return redirect('birthday:eventtype')
    else:
        form = ForWhomForm()

    return render(request, 'birthday/select.html', {'form': form})


def eventtype(request):
    if request.method == "POST":
        form = EventTypeForm(request.POST or None)
        if form.is_valid():
            name_obj = request.POST.get('name')
            #print()
            price = 0.00
            if name_obj[:1]== 'V':
                price = 12.00
            elif name_obj[:1]== 'B':
                price = 102.00
            elif name_obj[:1]== 'C':
                price = 1222.00
            elif name_obj[:1]== 'D':
                price = 1112.00
            elif name_obj[:1]== 'P':
                price = 152.00
            elif name_obj[:1]== 'S':
                price = 1332.00
                
            name_obj = EventType(
                name = name_obj,
                dam = price
            )
            name_obj.save()
            return redirect('birthday:guest')
    else:
        form = EventTypeForm()

    return render(request, 'birthday/event_types.html', {'form': form})

def guest_number(request):
    if request.method == "POST":
        form = GuestNumberForm(request.POST or None)
        if form.is_valid():
            name_obj = request.POST.get('number')
            #name_obj = int(name_obj) * 10
            price = int(name_obj) * 5
            name_obj = Guest(
                number = name_obj,
                price   = price
            )
            name_obj.save()
            return redirect('birthday:date')
    else:
        form = GuestNumberForm()

    return render(request, 'birthday/guest_number.html', {'form': form})

def select_date(request):
    if request.method == 'POST':
        form = DateInputForm(request.POST or None)
        if form.is_valid():
            date = request.POST.get('date')
            date = HelloDate(
                date = date,
            )
            date.save()
            return redirect('birthday:detail')
    else:
            form = DateInputForm()
    c = {
        'form': form,
    }
    return render(request, 'birthday/select_date.html', c)

def selection_detail(request):
    forwhom     = ForWhom.objects.all().order_by('-id')[0:1]
    eventtype   = EventType.objects.all().order_by('-id')[0:1]
    guest       = Guest.objects.all().order_by('-id')[0:1]
    date        = HelloDate.objects.all().order_by('-id')[0:1]
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    args = {
        'forwhom' : forwhom, 
        'eventtype' : eventtype,
        'guest' : guest,
        'date' : date,
        'cart_obj' : cart_obj
    }
    #print(args)
    return render(request, 'birthday/detail.html', args)