from .models import HotelPage
from wagtail_modeltranslation.translation import TranslationOptions
from wagtail_modeltranslation.decorators import register


@register(HotelPage)
class HotelPageTR(TranslationOptions):
    fields = (
        'title', 'body'
    )
