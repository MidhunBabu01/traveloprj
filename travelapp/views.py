from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,newsblog


def fun(request):
    obj = Place.objects.all()
    obj2 = newsblog.objects.all()
    return render(request,"index.html", {'place':obj,'blog':obj2})




