from django.shortcuts import render

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Vinícius',
    })

def recipe(request, id):

    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Vinícius',
    })