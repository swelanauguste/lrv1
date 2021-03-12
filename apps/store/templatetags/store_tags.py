from django import template

from ..models import Store

register = template.Library()


@register.simple_tag
def total_orders():
    return Store.objects.count()


@register.simple_tag
def orders_searching():
    return Store.objects.filter(status="searching").count()


@register.simple_tag
def orders_printed():
    return Store.objects.filter(status="printed").count()


@register.simple_tag
def orders_delivered():
    return Store.objects.filter(status="delivered").count()


@register.simple_tag
def orders_stamped():
    return Store.objects.filter(status="stamped").count()
