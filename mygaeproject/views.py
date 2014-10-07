__author__ = 'sunnyone'

from django.shortcuts import render
from django.core.context_processors import csrf


def home(request):
    context = {}
    context.update(csrf(request))
    context['user'] = request.user
    template = "home.html"
    return render(request, template, context)

def aboutus(request):
    context = {}
    template = "aboutus.html"
    return render(request, template, context)


def thankyou(request):
    context = {}
    template = "thankyou.html"
    return render(request, template, context)

