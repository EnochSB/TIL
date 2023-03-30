from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 방법 1: 너무 길다
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()
    
    # 방법 2
    article = Article(title=title, content=content)
    # 저장 전 유효성 검사 가능
    article.save()

    # 방법 3: 작성을 잘했는지 검사를 할 수 없어 사용하지 않는다.
    # Article.objects.create(title=title, content=content)

    # article = Article.objects.get()
    # context = {
    #     'title': title,
    #     'content': content,
    # }
    # return render(request, 'articles/create.html')
    return redirect('articles:detail', article.pk)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect('articles:detail', article.pk)