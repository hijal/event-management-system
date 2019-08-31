from django.urls import path
from .views import cart_home, cart_update, cart_guest_update, cart_forwhom_update, cart_date_update, checkout_home, checkout_done



urlpatterns = [ 
    path('', cart_home, name = 'home'),
    path('update/', cart_update, name = 'update'),
    path('checkout/', checkout_home, name = 'checkout'),
    path('guest/update/', cart_guest_update, name = 'guest_update'),
    path('checkout/success/', checkout_done, name = 'success'),
    path('forwhom/update/', cart_forwhom_update, name = 'forwhom_update'),
    path('date/update/', cart_date_update, name = 'date_update'),
]
