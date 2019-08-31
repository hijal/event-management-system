from django.shortcuts import render, redirect

from .models import Location, City, Place, Center
from .forms import PersonForm

def check(request):
    #list_places = Location.objects.all()
    if request.method == 'POST':
        form = PersonForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('birthday:select')
    else:
        form = PersonForm()
        
    c = {
        #'list_places' : list_places,
        'form' : form
    }
    return render(request, 'locations/location.html', c)

def load_cities(request):
    city_id = request.GET.get('city')
    places = Place.objects.filter(city_id=city_id)
    return render(request, 'locations/dropdown.html', {'places': places})

def load_com_center(request):
    place_id = request.GET.get('place')
    centers = Center.objects.filter(place_id=place_id)
    return render(request, 'locations/dropdown1.html', {'centers': centers})