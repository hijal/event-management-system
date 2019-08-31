
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import login_page, register_page, guest_register_view
from django.contrib.auth.views import LogoutView
from .views import home_page, about_page, gallery_page, contact_page
from addresses.views import checkout_address_create_view
from billing.views import payment_method_view, payment_method_create_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('gallery/', gallery_page, name='gallery'),
    path('contact/', contact_page, name='contact'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('billing/payment-method/', payment_method_view, name='billing-payment-method'),
    path('billing/payment-method/create/', payment_method_create_view, name='billing-payment-method-endpoint'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
    path('register/guest/', guest_register_view, name='guest_register'),
    path('location/', include(('locations.urls', 'locations'), namespace='location')), 
    path('item/', include(('items.urls', 'items'), namespace='item')),
    path('birthday/', include(('birthday.urls', 'birthday'), namespace='birthday')),
    path('cart/', include(('carts.urls', 'carts'), namespace='cart')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)