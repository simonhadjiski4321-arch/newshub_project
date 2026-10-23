from django import template

register = template.Library()


@register.filter
def word_count(value):
    return len(value.split())