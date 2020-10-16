from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from django.template.defaultfilters import floatformat

register = template.Library()

def currency(dollars):
    dollars = round(float(dollars), 2)
    return "$%s%s" % (intcomma(int(dollars)), ("%0.2f" % dollars)[-3:])

register.filter('currency', currency)


@register.filter
def percentage(number):
    value = float(number)
    if value is None:
        return None
    return floatformat(value, 2) + '%' 

register.filter('percentage', percentage)
