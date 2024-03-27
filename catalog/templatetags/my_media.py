from django import template

register = template.Library()


@register.simple_tag
def my_media(data):
    return data.url if data else '#'
