from django import template

register = template.Library()


@register.filter
def placeholder(field_obj, message):
    field_obj.field.widget.attrs['placeholder'] = message
    return field_obj
