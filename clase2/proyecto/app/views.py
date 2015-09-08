from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from datetime import datetime

def hora_actual(request):
    ahora = datetime.now()
    t = get_template('app/hora.html')
    c = Context({
        'hora': ahora,
        'usuario': 'Yoel'
    })

    html = t.render(c)

    return HttpResponse(html)
