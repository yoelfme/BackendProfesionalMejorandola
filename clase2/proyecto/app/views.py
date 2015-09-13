from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from .models import Enlace, Categoria
from .forms import *
from django.views.generic import ListView


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
            enlace = form.save(commit=False)
            enlace.usuario = request.user
            enlace.save()
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


class EnlaceListView(ListView):
    model = Enlace
    template_name = 'app/index.html'
    context_object_name = 'enlaces'
