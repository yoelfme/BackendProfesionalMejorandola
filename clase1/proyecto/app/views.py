from django.shortcuts import render
from django.http import HttpResponse
import urllib2
import json

# Create your views here.
def home(request):
    return HttpResponse("Pantalla Index")

def home2(request):
    return HttpResponse("Otro Home 2")

def post(request, id_post):
    return HttpResponse("Este es el post %s" % id_post)

def api(request):
    try:
        f = urllib2.urlopen("http://congresorest.appspot.com/diputado/1")
        g = f.read()
        f.close()
    except HTTPError, e:
        print "Error!!"
        print e.code
    except URLError, e:
        print "Error!!"
        print e.code

    dictionario = json.loads(g)

    return HttpResponse(dictionario["entidad"])
