from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
#my custom
from django.http import HttpResponse
# from templates import *
# Create your views here.
def test(request):
    name = "pavelave"
    names = ['pavel' , 'erza' , 'rize']
    return HttpResponse('erazz')