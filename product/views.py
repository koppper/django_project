from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotModified, \
    HttpResponseNotFound, HttpResponseBadRequest, HttpResponseNotAllowed
from django.shortcuts import render
from django.template.response import TemplateResponse
from .forms import StudentForms

# def index(request):
#     return render(request, "product/first_page.html")


# def second_page(request):
#     return HttpResponse("<h1> SkyLearn! </h1>")
#
#
# def skylearn_students(request, name="People", age=0):     # students/name/age/
#     return HttpResponse(f"<h2> Наши студенты </h2>"
#                         f"<p> Имя: {name}  </p>"
#                         f"<p> Возраст: {age} </p>")
#
#
# def students(request):
#     name = request.GET.get("name")
#     age = request.GET.get("age")
#     return HttpResponse(f"<h2> Наши студенты </h2>"
#                         f"<p> Имя: {name}  </p>"
#                         f"<p> Возраст: {age} </p>")
#
#
# def products(request):
#     category = request.GET.get("category", "Category Product")
#     name = request.GET.get("name", "Product Name")
#     price = request.GET.get("price", 0)
#
#     return render(request, "product/first_page.html", context={"category": category, "name": name, "price": price})
#
# def index(request):
#     return HttpResponse("Hello World!")
#
#
# def block(request):
#     return HttpResponse("/Block/")
#
#
# def redirect_(request):
#     return HttpResponseRedirect("/block")
#
#
# def permanent_redirect(request):
#     return HttpResponsePermanentRedirect("/")
#
#
# def m304(request):
#     return HttpResponseNotModified()
#
#
# def m404(request):
#     return HttpResponseNotFound('<h1> Ошибка 404 </h>')
#
#
# def m400(request):
#     return HttpResponseBadRequest()
#
#
# def m405(request):
#     return HttpResponseNotAllowed("<h1> Not Allowed </h1>")
#
#
# def students(request, i):
#     students = ['Bob', 'Sam', 'Tom']
#     if i in range(len(students)):
#         return HttpResponse(students[i])
#     else:
#         return HttpResponseNotFound()
#

def index(request):
    message = '*Наше сообщение*'
    skylearn = 'Курсы программирование'
    data = {"message": message, "skylearn": skylearn}
    return render(request, "product/first_page.html", context=data)


###########################3
def products(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        address = request.POST.get("address")
        langs = request.POST.get("langs")
        return HttpResponse(f"<h2>{name}</h2>"
                            f"<h2>{age}</h2>"
                            f"<h2>{address}</h2>"
                            f"<h2>{langs}</h2>")
    else:
        form = StudentForms()
        return render(request, "product/products.html", context={"form": form})
#################################


def students(request):
    return render(request, "product/students.html")
