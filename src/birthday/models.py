from django.db import models
from datetime import datetime



class ForWhom(models.Model):
    select = models.CharField(max_length = 15)

    def __str__(self):
        return self.select


class EventType(models.Model):
    name = models.CharField(max_length = 150)
    dam   = models.DecimalField(max_digits=20,  decimal_places=2, default = 0.00)
    
    def __str__(self):
        return self.name

class Guest(models.Model):
    number  = models.CharField(max_length = 100)
    price   = models.DecimalField(max_digits=20,  decimal_places=2, default = 5.00)

    def __str__(self):
        return self.number

class HelloDate(models.Model):
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return  str(self.date)