from django.db import models


class EventManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


class Event(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    objects = EventManager()

    def get_absolute_url(self):
        return "/events/{id}/".format(id=self.id)

    def __str__(self):
        return self.title

