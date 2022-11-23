from django.shortcuts import render, redirect
from .forms import UserForm
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        return HttpResponse(f"<h2> Привет, {name}. Твой возраст: {age} </h2>")
    else:
        userform = UserForm()
        return render(request, "skylearn/base.html", context={"form": userform})


def skylearn(request):
    return render(request, "skylearn/skylearn.html")


def post_z(request):
    name = request.POST.get("name")
    age = request.POST.get("age")
    return HttpResponse(f"<h2> Привет, {name}. Твой возраст: {age} </h2>")
