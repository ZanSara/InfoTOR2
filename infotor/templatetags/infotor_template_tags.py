from django import template

register = template.Library()

@register.inclusion_tag('infotor/navbar.html')
def render_navbar():
    return {}

@register.inclusion_tag('infotor/sidebar.html')
def render_sidebar():
    return {}

@register.inclusion_tag('infotor/sidebar_forra.html')
def render_sidebar_forra():
    return {}

@register.filter
def as_time(value):
    if value is None:
        return "--:--"
    return str(value).replace('.', ':')
    
@register.filter
def as_minutes(value):
    if value is None:
        return "--:--"
    minuti = int(value) % 60
    ore = int(int(value) / 60 )
    return "{}:{}".format(ore, minuti)
    
@register.filter
def minus(value, arg):
    return int(value) - int(arg)
    
    
@register.filter
def value_or_dashes(value):
    if value is None:
        return "---"
    return value

@register.filter
def value_or_dashes_time(value):
    if value is None:
        return "--:--"
    return value
    
@register.filter
def value_or_noinfo(value):
    if value is None:
        return "(Nessuna informazione)"
    return value
