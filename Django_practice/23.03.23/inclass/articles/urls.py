from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('<int:num>/', views.detail, name='detail'),
    path('hello/<name>/', views.greeting, name='greeting'),
]
