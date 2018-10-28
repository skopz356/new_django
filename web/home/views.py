import pathlib
import socket
from subprocess import call, check_output
from urllib import request
from .models import Page, Subject
from django.contrib.auth.views import TemplateView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from engine.ips import map_network
from engine.logs import writeLogs
from home.apps import HomeConfig


template_dir = HomeConfig.name


# Create your views here.
'''  '''


def index(request):
    request.session["ip"] = map_network()
    q = Page.objects.get(pk=1)
    arg = {'content': q.content,
           # 'page':q
           }
    return render(request, 'home/index.html', arg)


def page(request, page):
    p = get_object_or_404(Page, title=page)
    s = get_object_or_404(Subject, name="Neco")
    arg = {'page': p,
           'product': s
           }
    return render(request, 'home/index.html', arg)


def pageview(request, page):
    if request.GET.get("ipButton"):
        writeLogs(request.GET.get("ip"))
    args = {
        "ips": map_network()
    } 
    return render(request, template_dir+"/index.html", args )


    

