from django.shortcuts import render
from django.template.response import TemplateResponse


def ext(request):
    return render(request, "index.html", context={"site": "SKYLEARN"})