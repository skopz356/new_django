from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    numbers = [5,6,7,8]
    arg = {'numbers':numbers}
    return render(request,'home/index.html',arg)