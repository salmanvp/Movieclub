from django.shortcuts import render
from .models import Movies
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def home(request):
    b = Movies.objects.all()
    return render(request, 'home.html', {'b': b})


# class home(ListView):
#     model = Movies
#     template_name = 'home.html'
#     context_object_name = 'b'


def add(request):
    if (request.method == 'POST'):
        name = request.POST['moviename']
        desc = request.POST['description']
        image = request.FILES['img']
        a = Movies.objects.create(name=name, desc=desc, image=image)
        a.save()
        return home(request)
    return render(request, 'add.html')


def details(request, p):
    d = Movies.objects.get(slug=p)
    return render(request, 'details.html', {'d': d})


def delete(request, l):
    a = Movies.objects.get(slug=l)
    a.delete()
    return home(request)


def edit(request, e):
    a = Movies.objects.get(slug=e)
    if (request.method == 'POST'):
        na = request.POST['moviename']
        de = request.POST['description']
        im = request.FILES['img']
        a.name = na
        a.desc = de
        a.image = im
        a.save()
        return home(request)
    return render(request, 'edit.html', {'a': a})
