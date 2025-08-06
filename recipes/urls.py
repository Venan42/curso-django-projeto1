from django.urls import path

<<<<<<< HEAD
from recipes.views import home


urlpatterns = [
    path('', home)
=======
from recipes.views import home, contato, sobre


urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre)
>>>>>>> 59bef86f54f829625f039fe496f587cd413314f4
]