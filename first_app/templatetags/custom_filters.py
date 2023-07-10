from django import template

register = template.Library()

@register.filter(name='callme')
def callme(value, arg):
    return (value+' '+arg).title()

# register.filter('callme',callme)
