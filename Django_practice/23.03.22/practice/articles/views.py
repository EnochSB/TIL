from django.shortcuts import render
import random

# Create your views here.
def today_dinner(request):
    foods = ['햄버거', '치킨', '피자', '제육볶음', '돈까스', '보쌈', '족발', '떡볶이', '김밥', '라면', '카레', '순두부찌개', '김치찌개']
    dinner = random.choice(foods)
    content = {
        'dinner': dinner,
    }
    return render(request, 'articles/today_dinner.html', content)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    content = {
        'message': request.GET.get('message')
    }
    return render(request, 'articles/catch.html', content)

def lotto_create(request):
    return render(request, 'articles/lotto_create.html')

def lotto(request):
    n = int(request.GET.get('message'))
    numbers = range(1, 46)
    lotto_list = []
    for _ in range(n):
        lotto_list.append(random.sample(numbers, 6))
    content = {
        'lotto_list': lotto_list,
    }
    return render(request, 'articles/lotto.html', content)