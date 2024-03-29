from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    # DB에 전체 게시글 조회를 요청하고 쿼리셋을 응답받아 저장
    articles = Article.objects.all()
    # print(articles)
    context = {
        'articles': articles,
    }

    # context - 템플릿에 데이터와 함께 렌더링
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    # print(article)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)


# def create(request):
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')
#     # article = Article(title=title, content=content)
#     # article.save()
#     form = ArticleForm(request.POST)
#     if form.is_valid():
#         article = form.save()
#         return redirect('articles:detail', article.pk)
#     context = {
#         'form': form
#     }
#     return render(request, 'articles/new.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def delete(request, artilce_pk):
    article = Article.objects.get(pk=artilce_pk)
    article.delete()

    return redirect('articles:index')


# def edit(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form': form
#     }
#     return render(request, 'articles/edit.html', context)


# def update(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')
#     # article.title = title
#     # article.content = content
#     # article.save()
#     form = ArticleForm(request.POST, instance=article)
#     if form.is_valid():
#         form.save()
#         return redirect('articles:detail', article_pk)
#     context = {
#         'article': article,
#         'form': form,
#     }

#     return render(request, 'articles/edit.html', context)


def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article_pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form
    }
    return render(request, 'articles/update.html', context)