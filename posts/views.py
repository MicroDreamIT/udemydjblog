from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('index')


# Create your views here.
def show(request, id):
    return HttpResponse('show')


# Create your views here.
def edit(request, id):
    return HttpResponse('edit')


# Create your views here.
def delete(request, id):
    return HttpResponse('delete')


