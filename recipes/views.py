from django.shortcuts import render
from django.http import HttpResponse

def home(request):
<<<<<<< HEAD
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Vinícius'
    })

=======
    return render(request, 'home.html')


def contato(request):
    return HttpResponse('contato')

def sobre(request):
    return HttpResponse('sobre')
>>>>>>> 59bef86f54f829625f039fe496f587cd413314f4
