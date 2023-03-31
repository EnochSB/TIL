from django.shortcuts import render, redirect
from .models import AccountBook

# Create your views here.

def index(request):
    if request.method == 'POST':
        category_target = request.POST.get('category_target')
        if category_target:
            accounts = AccountBook.objects.filter(category=category_target)
        else:
            accounts = AccountBook.objects.all()
    else:
        category_target = request.GET.get('category_target')
        if category_target:
            accounts = AccountBook.objects.filter(category=category_target)
        else:
            accounts = AccountBook.objects.all()
    
    sort = request.GET.get('sort', 'note')
    amount_order = request.GET.get('amount_order', '오름차순')
    date_order = request.GET.get('date_order', '오름차순')
    if sort == 'amount':
        if amount_order == '내림차순':
            accounts = accounts.order_by(sort)
            amount_order = '오름차순'
        else:
            accounts = accounts.order_by(f'-{sort}')
            amount_order = '내림차순'
    elif sort == 'date':
        if date_order == '내림차순':
            accounts = accounts.order_by(sort)
            date_order = '오름차순'
        else:
            accounts = accounts.order_by(f'-{sort}')
            date_order = '내림차순'

    context = {
        'accounts': accounts,
        'amount_order': amount_order,
        'date_order': date_order,
        'category_target': category_target,
    }
    return render(request, 'accountbooks/index.html', context)


def detail(request, pk):
    account = AccountBook.objects.get(pk=pk)
    context ={
        'account': account,
    }
    return render(request, 'accountbooks/detail.html', context)


def new(request):
    return render(request, 'accountbooks/new.html')


def create(request):
    note = request.POST.get('note')
    category = request.POST.get('category')
    amount = request.POST.get('amount')
    date = request.POST.get('date')
    description = request.POST.get('description')
    account = AccountBook(note=note, category=category, amount=amount, date=date, description=description)
    account.save()
    return redirect('accountbooks:detail', account.pk)


def delete(request, pk):
    account = AccountBook.objects.get(pk=pk)
    account.delete()
    return redirect('accountbooks:index')


def edit(request, pk):
    account = AccountBook.objects.get(pk=pk)
    context = {
        'account': account,
    }
    return render(request, 'accountbooks/edit.html', context)


def update(request, pk):
    account = AccountBook.objects.get(pk=pk)
    account.note = request.POST.get('note')
    account.category = request.POST.get('category', account.category)
    account.amount = request.POST.get('amount')
    account.date = request.POST.get('date')
    account.description = request.POST.get('description')
    account.save()
    return redirect('accountbooks:detail', account.pk)


def copy(request, pk):
    account = AccountBook.objects.get(pk=pk)
    copy_account = AccountBook(note=account.note, category=account.category, amount=account.amount, date=account.date, description=account.description)
    copy_account.save()

    return redirect('accountbooks:index')

