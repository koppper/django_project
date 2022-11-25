from django.shortcuts import render
from django.http import HttpResponse
from .forms import Animals, People


def animals(request):
    if request.method == "POST":
        name = request.POST.get("name")
        people = request.POST.get("people")
        price = request.POST.get("price")
        image = request.POST.get("image")

        return HttpResponse(f"{name}, {people}, {price}, {image}")

    else:
        animalform = Animals
        return render(request, "animals.html", context={"form": animalform})


def people(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        animal = request.POST.get("animal")
        slug = request.POST.get("slug")
        pw = request.POST.get("pw")
        file = request.POST.get("file")
        return HttpResponse(f"{first_name}, {last_name}, {email}, {age}, {animal}, {slug}, {pw}, {file}")
    else:
        peopleform = People
        return render(request, "peoples.html", context={"forms": peopleform})
