from django import template

register = template.Library()


@register.filter()
def mymedia_filter(val):
    if val:

        return f'/media/{val}'
    return '#'


@register.simple_tag
def mymedia_tag(val):
    if val:
        return f'/media/{val}'
    return '#'


@register.filter()
def description_filter(val):
    if val:

        return f'{val}'[:500]
    return '#'


@register.filter()
def version_filter(val):
    if val.activate:

        return f'{val}'
    return '#'