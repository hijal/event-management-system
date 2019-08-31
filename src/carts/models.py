from django.conf import settings
from django.db import models

from birthday.models import ForWhom, EventType, Guest, HelloDate

User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get('cart_id', None)
        qs = self.get_queryset().filter(id = cart_id)

        if qs.count() == 1:
            new_obj = False
            #print('cart id exists')
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj
        
    def new(self, user = None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user = user_obj)


class Cart(models.Model):
    user        = models.ForeignKey(User, null = True, blank = True, on_delete = models.CASCADE)
    guest       = models.ManyToManyField(Guest)
    eventType   = models.ManyToManyField(EventType)
    forwhom     = models.ManyToManyField(ForWhom)
    date        = models.ManyToManyField(HelloDate)
    total       = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    objects = CartManager()

    def __str__(self):
        return str(self.id)


