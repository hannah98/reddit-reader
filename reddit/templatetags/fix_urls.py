from django import template
import re

register = template.Library()

@register.filter
def fixURL(string):
    line = re.sub(r"^https?://(www.)?reddit.com", "", string)
    return line

