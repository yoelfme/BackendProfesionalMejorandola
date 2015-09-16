from random import choice
from django.core.urlresolvers import reverse
from django.core.cache import cache

frases = ['Leonidas esta sentado', 'Freddy se fue', 'Christian esta arriba']


def ejemplo(request):
    frase = cache.get('frase_cool')
    if frase is None:
        frase = choice(frases)
        cache.set('frase_cool', frase)

    return {
        'frase': frase
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
