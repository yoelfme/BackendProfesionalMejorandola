from random import choice
from django.core.urlresolvers import reverse

frases = ['Leonidas esta sentado', 'Freddy se fue', 'Christian esta arriba']


def ejemplo(request):
    return {
        'frase': choice(frases)
    }


def menu(request):
    menu = {'menu': [
        {'name': 'Home', 'url': reverse('home')},
        {'name': 'Add', 'url': reverse('add')},
        {'name': 'About', 'url': reverse('about')},
    ]}

    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True

    return menu
