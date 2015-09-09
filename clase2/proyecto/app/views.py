from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def home(request):
    categorias = Categoria.objects.all()
    enlaces = Enlace.objects.all()
    template = "app/index.html"

    return render(request, template, {
        "categorias": categorias,
        "enlaces": enlaces
    })

def categoria(request, id_categoria):
    categorias = Categoria.objects.all()
    cat = get_object_or_404(Categoria, pk=id_categoria)
    enlaces = Enlace.objects.filter(categoria=cat)
    template = "app/index.html"

    return render(request, template, {
        "categorias": categorias,
        "enlaces": enlaces
    })

@login_required
def minus(request, id_enlace):
    enlace = Enlace.objects.get(pk=id_enlace)
    enlace.votos -= 1
    enlace.save()
    return HttpResponseRedirect("/")

@login_required
def plus(request, id_enlace):
    enlace = Enlace.objects.get(pk=id_enlace)
    enlace.votos += 1
    enlace.save()
    return HttpResponseRedirect("/")

@login_required
def add(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = EnlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = EnlaceForm()

    template = 'app/form.html'
    return render(request, template,
                  context_instance=RequestContext(request, locals()))

def hora_actual(request):
    # ahora = datetime.now()
    # t = get_template('app/hora.html')
    # c = Context({
    #     'hora': ahora,
    #     'usuario': 'Yoel'
    # })
    #
    # html = t.render(c)

    now = datetime.now()

    return render(request, 'app/hora.html', {
        'hora': now,
        'usuario': 'Yoel'
    })
