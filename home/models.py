from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail_modeltranslation.models import TranslationMixin
from ckeditor.fields import RichTextField


class HomePage(Page):
    pass


COUNTRY_CHOICES = (
    ('Poland', _('Poland')),
    ('Slovakia', _('Slovakia')),
    ('Czech Republic', _('Czech Republic')),
    ('Hungary', _('Hungary'))
)


class HotelPage(TranslationMixin, Page):
    city = models.CharField(verbose_name=_('City'), max_length=128)
    country = models.CharField(verbose_name=_('Country'),
                               choices=COUNTRY_CHOICES,
                               default='COUNTRY.SLOVAKIA',
                               max_length=64)
    body = RichTextField(verbose_name=_('Content'), blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('city'),
        FieldPanel('country'),
        FieldPanel('body'),
    ]