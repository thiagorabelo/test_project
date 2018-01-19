from django.shortcuts import render, get_object_or_404
from .models import Foo

# Create your views here.

def foo(request, foo_id=None):
    if foo_id:
        foo = get_object_or_404(Foo, pk=foo_id)
        foos = [foo]
    else:
        foos = Foo.objects.all()
    
    return render(request, 'foo/foo.html', {'foos': foos})

