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
    return str(value).replace('.', ':')
    
