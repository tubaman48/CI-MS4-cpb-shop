""" bag_tools template """

from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Calculate subtotal """
    return price * quantity
