from django import template
from inventory.models import Phone, Brand

register = template.Library()

@register.filter(name='is_phone')
def is_phone(obj):
    return isinstance(obj, Phone)

@register.filter(name='is_brand')
def is_brand(obj):
    return isinstance(obj, Brand)
