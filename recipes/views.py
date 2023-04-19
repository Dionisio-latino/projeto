# from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('HOME')


def sobre(request):
    return HttpResponse('sobre')


def contatos(request):
    return HttpResponse('contatos')
