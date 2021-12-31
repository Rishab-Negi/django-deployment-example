from django import template
register = template.Library()

def cut(value, arg):
    """
    tHIS CUTS OUT ALL THE VALUES OF "ARG" FROTHE STRING!
    """
    return value.replace(arg, "")

register.filter('cut', cut)
