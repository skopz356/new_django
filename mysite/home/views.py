from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from .models import Page,Subject 

# Create your views here.
'''  '''
def index(request):
    numbers = [5,6,7,8]
    q= Page.objects.get(pk=1)
    arg = {'mainpage':'you are on the main page',
    #'page':q    
    }
    return render(request,'home/index.html',arg)

def page(request,page):
    p = get_object_or_404(Page, title=page)
    s = get_object_or_404(Subject, name="Neco")
    arg = {'page':p,
    'product':s
    }
    return render(request, 'home/index.html', arg)
