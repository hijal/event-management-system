from django.shortcuts import render, redirect
from .models import Cart
from birthday.models import Guest, EventType, ForWhom, HelloDate
from orders.models import Order
from accounts.forms import LoginForm, GuestForm
from billing.models import BillingProfile
from accounts.models import GuestEmail
from addresses.forms import AddressForm
from addresses.models import Address
from django.conf import settings

import stripe
STRIPE_API_KEY = getattr(settings, 'STRIPE_API_KEY', 'sk_test_cY4XZIL4hfYUlIOhhu2uPwQy00KCFuc0yS')
STRIPE_PUB_KEY = getattr(settings, 'STRIPE_PUB_KEY', 'pk_test_Vh4kodVKVBPiediz9paREiJq00fxuNLEyD')
stripe.api_key = STRIPE_API_KEY


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    #print(cart_obj)
    guests = cart_obj.guest.all().order_by('-id')[0:1]
    eventcost = cart_obj.eventType.all().order_by('-id')[0:1]
    forwhom = cart_obj.forwhom.all().order_by('-id')[0:1]
    date = cart_obj.date.all().order_by('-id')[0:1]
    #print(guests)
    total = 0
    for x in guests:
        total += x.price
    
    for x in eventcost:
        total += x.dam
    cart_obj.total = total
    cart_obj.save()
    print(total)
    return render(request, 'carts/home.html', {'cart' : cart_obj})

def cart_guest_update(request):
    #print(request.POST)
    guestId = request.POST.get('guest_id')
    guest_obj = Guest.objects.get(id = guestId)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if guest_obj in cart_obj.guest.all():
        cart_obj.guest.remove(guest_obj)
    else:
        cart_obj.guest.add(guest_obj)
    return redirect('birthday:detail')

def cart_update(request):
    #print(request.POST)
    eventId = request.POST.get('event_id')
    event_obj  = EventType.objects.get(id = eventId)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if event_obj in cart_obj.eventType.all():
        cart_obj.eventType.remove(event_obj)
    else:
        cart_obj.eventType.add(event_obj)
    return redirect('birthday:detail')

def cart_forwhom_update(request):
    forwhomId = request.POST.get('forwhom_id')
    forwhom_obj  = ForWhom.objects.get(id = forwhomId)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if forwhom_obj in cart_obj.forwhom.all():
        cart_obj.forwhom.remove(forwhom_obj)
    else:
        cart_obj.forwhom.add(forwhom_obj)
    return redirect('birthday:detail')

def cart_date_update(request):
    dateId = request.POST.get('date_id')
    date_obj  = HelloDate.objects.get(id = dateId)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if date_obj in cart_obj.date.all():
        cart_obj.date.remove(date_obj)
    else:
        cart_obj.date.add(date_obj)
    return redirect('birthday:detail')


def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created:
        return redirect('cart:home')
   
    login_form = LoginForm()
    guest_form = GuestForm()
    address_form = AddressForm()
    billing_address_id = request.session.get('billing_address_id', None)
    shipping_address_id = request.session.get('shipping_address_id', None)


    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    # guest_email_id = request.session.get('guest_email_id')
    # billing_profile = None
    # if user.is_authenticated:
    #     billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(user=user, email=user.email)

    # elif guest_email_id is not None:
    #     guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
    #     billing_profile, billing_guest_profile_created = BillingProfile.objects.get_or_create(email=guest_email_obj.email)
    # else:
    #     pass

    has_card = False 
    if billing_profile is not None:
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
        if shipping_address_id:
            order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
            del request.session['shipping_address_id']
        if billing_address_id:
            order_obj.billing_address = Address.objects.get(id=billing_address_id)
            del request.session['billing_address_id']
        if billing_address_id or shipping_address_id:
            order_obj.save()
        has_card = billing_profile.has_card


    if request.method == "POST":
        is_prepared = order_obj.check_done()
        if is_prepared:
            did_charge, crg_msg = billing_profile.charge(order_obj)
            if did_charge:
                order_obj.mark_paid() 
                del request.session['cart_id']
                if not billing_profile.user:
                    billing_profile.set_cards_inactive()
                return redirect("cart:success")
            else:
                #print(crg_msg)
                return redirect("cart:checkout")

    args = {
        'object': order_obj,
        'billing_profile' : billing_profile,
        'login_form' : login_form,
        'guest_form' : guest_form,
        'address_form' : address_form,
        "has_card": has_card,
        'publish_key': STRIPE_PUB_KEY,

    }
    return render(request, 'carts/checkout.html', args)

def checkout_done(request):
    return render(request, 'carts/checkout_done.html', {})