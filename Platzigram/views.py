"""Modulo de Hello world"""

from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello world.')