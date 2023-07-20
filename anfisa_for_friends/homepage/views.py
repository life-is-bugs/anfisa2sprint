from django.shortcuts import render
from ice_cream.models import IceCream
from django.db.models import Q

def index(request):
    ice_cream_list = IceCream.objects.values('id', 'title', 'description', c'category__title')
    template = 'homepage/index.html'
    # Запишите в переменную ice_cream_list новый QuerySet
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)
