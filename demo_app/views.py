# Create your views here.
from .models import Product
from django.shortcuts import render


def home(request, template_name='home.html'):
    """ This renders the home page"""
    context = {}
    return render(request, template_name, context)


def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        raw_query_string = query.split('&')
        products = []

        for string in raw_query_string:
            key = ''
            value = ''

            key_value = string.split(':')
            if key_value[0].strip():
                key = key_value[0].strip()
            if len(key_value) is 2:
                if key_value[1].strip():
                    value = key_value[1].strip()

            p = Product.objects.filter(product_properties__name=key,
                                       product_properties__value=value)
            products += p

        results = list(set(products))

    return render(request,
                  'search/search.html',
                  {'results': results,
                   'query': query})
