
from django.template import Library
from django.utils import six


register = Library()


_obj_getattr = object.__getattribute__
_obj_setattr = object.__setattr__

# based on: http://code.activestate.com/recipes/496741-object-proxying/
@six.python_2_unicode_compatible
class _BoundFieldProxy(object):
    __slots__ = ['_the_field', '_the_attrs', '_the_original_obj']

    def __init__(self, field, attrs=None):
        _obj_setattr(self, '_the_field', field)
        _obj_setattr(self, '_the_attrs', attrs or {})

        try:
            original_obj = _obj_getattr(field, '_the_original_obj')
        except AttributeError:
            original_obj = field

        _obj_setattr(self, '_the_original_obj', original_obj)

    def __str__(self):
        original_obj = _obj_getattr(self, '_the_original_obj')
        return original_obj.__class__.__str__(self)

    def as_widget(self, widget=None, attrs=None, only_initial=False):
        instance_attrs = _obj_getattr(self, '_the_attrs')

        if isinstance(attrs, dict):
            instance_attrs.update(attrs)

        return _obj_getattr(self, '_the_field').as_widget(widget=widget,
                                                          attrs=instance_attrs,
                                                          only_initial=only_initial)

    def __getattr__(self, name):
        _field = _obj_getattr(self, '_the_field')
        return getattr(_field, name)

    def __setattr__(self, name, value):
        return _obj_setattr(_obj_getattr(self, '_the_field'), name, value)

    def __del__(self):
        print("I'm dying")


@register.filter
def attr(field, attrs):
    parameters = attrs.split(':', 1)
    attribute = parameters[0]
    value = parameters[1] if len(parameters) == 2 else ''

    return _BoundFieldProxy(field, {attribute: value})


@register.filter
def add_class(field, classes):
    return _BoundFieldProxy(field, {'class': classes})


@register.filter
def dunder(field, name):
    return getattr(field, f'__{name}__')
