from django.urls import path, re_path
from .views import index, products, students
# from .views import second_page, skylearn_students, students, products
# from .views import index, block, redirect_, permanent_redirect, m304, m404, m400, m405, students


urlpatterns = [
    # path('', index),
    # path('block/', block),
    # path('redirect/', redirect_),
    # path('permanent_redirect/', permanent_redirect),
    # path('m304/', m304),
    # path('m404/', m404),
    # path('m400/', m400),
    # path('m405/', m405),
    # path('students/<int:i>', students)
    path('', index, name='home'),
    path('products/', products),
    path('students/', students, name='students')
]















# urlpatterns = [
#     # # path('', index, name='home'),
#     # re_path(r'^page/\w', second_page, name="second_page"),
#     # # path('students/', skylearn_students),
#     # # path('students/<str:name>/', skylearn_students),
#     # path('students/<str:name>/<int:age>/', skylearn_students),
#     #
#     #
#     #
#     # path('students/', students),
#     # path('product/', products, name="products")
# ]


# ^ начало текста
# $ конец текста
# \d цифра
# \w текст
#
# \d+ цифра
# \w+ текст

# path(route, view, kwargs=None, name=None)
# re_path(route, view, kwargs=None, name=None)


# str /
# int
# slug  asd-sad-fdsfdsf445-fdsf
# uuid  1 2 3     4l564-45465-45666666666dsadsadsadsadwqeqw
# path  /
