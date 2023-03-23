from django.shortcuts import render

# Create your views here.
def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    message = request.GET.get('message')
    content = {
        'message': message,
    }
    return render(request, 'articles/catch.html', content)


def number_print(request, number):
    content = {
        'number': number,
    }
    return render(request, 'articles/number_print.html', content)


def calculate(request, number1, number2):
    content = {
        'number1': number1,
        'number2': number2,
        'plus': number1 + number2,
        'minus': number1 - number2,
        'multiple': number1 * number2,
        'divide': number1 // number2,
    }
    return render(request, 'articles/calculate.html', content)