from django.db import models
from courses.models import Room
from django.db.models.fields import BooleanField
import datetime
from django.utils.translation import ugettext as _

from django.conf import settings

import django.contrib.auth as auth

from . import managers
from django.core.exceptions import ValidationError
from courses.services import calculate_relevant_experience, format_prices
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField


class Organise(models.Model):
    organiser = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='organising')
    event = models.ForeignKey('Event', related_name='organising')

    def __str__(self):
        return"{} organises {}".format(self.organiser, self.event)


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255, blank=False)
    name.help_text = "The name of this event (e.g. 'Freies Tanzen')"
    date = models.DateField()
    time_from = models.TimeField(blank=True, null=True)
    time_to = models.TimeField(blank=True, null=True)
    room = models.ForeignKey(Room, related_name='events', blank=True, null=True, on_delete=models.SET_NULL)
    price_with_legi = models.FloatField(blank=True, null=True)
    price_with_legi.help_text = "Leave this empty for free entrance"
    price_without_legi = models.FloatField(blank=True, null=True)
    price_without_legi.help_text = "Leave this empty for free entrance"
    price_special = models.CharField(max_length=255, blank=True, null=True)
    price_special.help_text ="Set this only if you want a different price schema."
    organisators = models.ManyToManyField(settings.AUTH_USER_MODEL, through=Organise, related_name='organising_events')
    description = HTMLField(blank=True, null=True)
    special = BooleanField(blank=True, null=False, default=False)
    special.help_text = "If this is a special event that should be emphasized on the website"
    display = models.BooleanField(default=True)
    display.help_text = "Defines if this event should be displayed on the website."
    image = FilerImageField(blank=True, null=True)
    image.help_text ="Advertising image for this event."

    objects = models.Manager()
    displayed_events = managers.DisplayedEventManager()
    special_events = managers.SpecialEventManager()

    def format_organisators(self):
        return ', '.join(map(auth.get_user_model().get_full_name, self.organisators.all()))

    format_organisators.short_description = "Organisators"

    def format_prices(self):
        return format_prices(self.price_with_legi, self.price_without_legi, self.price_special)

    format_prices.short_description = "Prices"

    def format_time(self):
        if self.time_from and self.time_to:
            return"{}-{}".format(self.time_from.strftime("%H:%M"), self.time_to.strftime("%H:%M"))
        elif self.time_from:
            return"ab {}".format(self.time_from.strftime("%H:%M"))
        else:
            return"unbekannt"

    format_time.short_description = "Time"

    def __str__(self):
        return"{}".format(self.name)

    class Meta:
        ordering = ['date', 'time_from', 'room']
