from django.shortcuts import render
#my custom
from django.http import HttpResponse
# from templates import *
# Create your views here.
def test(request):
    name = "pavelave"
    names = ['pavel' , 'erza' , 'rize']
    return render(request , 'blog/index.html' , context={"name" : name , "nam" : names})