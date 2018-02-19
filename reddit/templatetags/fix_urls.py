from django import template
import re

register = template.Library()

@register.filter
def fixURL(string):
    line = re.sub(r"^https?://(www.)?reddit.com", "", string)
    return line

@register.filter("print_timestamp")
def print_timestamp(timestamp):
    try:
        #assume, that timestamp is given in seconds with decimal point
        ts = float(timestamp)
    except ValueError:
        return None
    return datetime.fromtimestamp(ts)

@register.filter
def age(value):
    now = datetime.now()
    try:
        ts = float(value)
        finalts = datetime.fromtimestamp(ts)
        difference = now - finalts
    except:
        return 'some time ago'

    if difference <= timedelta(minutes=1):
        return 'just now'
    return '%(time)s ago' % {'time': timesince(finalts).split(', ')[0]}
