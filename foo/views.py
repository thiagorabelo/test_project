from django.shortcuts import render, get_object_or_404
from .models import Foo
from .forms import CoisaForm

# Create your views here.


def foo(request, foo_id=None):
    if foo_id:
        foo_ = get_object_or_404(Foo, pk=foo_id)
        foos = [foo_]
    else:
        foos = Foo.objects.all()

    form = CoisaForm()

    return render(request, 'foo/foo.html', {'foos': foos, 'form': form})
