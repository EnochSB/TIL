from django.shortcuts import render
import random

# Create your views here.
def index(request):
    context = {
        'name' : 'enoch',
    }
    return render(request, 'articles/index.html', context)

def dinner(request):
    foods = ['족발', '햄버거', '치킨', '초밥',]
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked,
    }
    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    content = {
        'message': request.GET.get('message'),
    }
    return render(request, 'articles/catch.html', content)