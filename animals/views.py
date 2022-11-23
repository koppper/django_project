from django.shortcuts import render
from django.http import HttpResponse


def animals(request):
    return HttpResponse("ANIMALS")
