# Create your views here.


from django.shortcuts import render


def home(request, template_name='home.html'):
    """ This renders the home page"""
    context = {}
    return render(request, template_name, context)
