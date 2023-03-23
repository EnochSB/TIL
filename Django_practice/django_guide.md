# 장고 개발 환경 설정 가이드
## 01. 가상환경 생성 / 활성화
```bash
# 생성
$ python -m venv venv

# 활성화
$ source venv/Scirpts/activate
# 소스 v/스크립트/액트
# deactive로 비활성화
```

## 02. django 설치
```bash
$ pip install django==3.2.18
# 3.2.18 = 최신버전
```

## 03. 의존성 파일 생성
```bash
$ pip freeze > requirements.txt
# 파이썬 프리즈 화살표
```

## 04. 프로젝트 생성
```bash
$ django-admin startproject pjtname .
# 장고-어드민 스타트프로젝트 프로젝트명 띄고 쩜(.)
```

## 05. 서버 실행 및 종료
```bash
$ python manage.py runserver
# 파이썬 매니지.py 런서버
```
- ctrl + C 로 끄기

## 06. 앱 생성
```bash
$ python manage.py startapp appnames
# 앱 이름은 복수형 권장
# 짧은 소문자. 숫자, 공백, 특수문자 포함하지 않게
```

## 07. 앱 등록
- 프로젝트 폴더 > settings.py > INSTALLED_APPS에 앱이름 작성
- 앱을 생성한 후에 등록(반대는 불가)
- local app, 3rd party app, 기본 django app 순서 권장

## 08. Secretkey 환경변수
- pip install django-environ
- .env 파일 생성
  ```env
  DEBUG=on
  SECRET_KEY=your-secret-key
  DATABASE_URL=psql://user:un-githubbedpassword@127.0.0.1:8458/database
  SQLITE_URL=sqlite:///my-local-sqlite.db
  CACHE_URL=memcache://127.0.0.1:11211,127.0.0.1:11212,127.0.0.1:11213
  REDIS_URL=rediscache://127.0.0.1:6379/1?client_class=django_redis.client.DefaultClient&password=ungithubbed-secret
  ```
- settings.py 조작
  ```python
  import environ
  import os

  env = environ.Env(
      # set casting, default value
      DEBUG=(bool, False)
  )

  # Set the project base directory
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

  # Take environment variables from .env file
  environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

  # False if not in os.environ because of casting above
  DEBUG = env('DEBUG')

  # Raises Django's ImproperlyConfigured
  # exception if SECRET_KEY not in os.environ
  SECRET_KEY = env('SECRET_KEY')

  # Parse database connection url strings
  # like psql://user:pass@127.0.0.1:8458/db
  DATABASES = {
      # read os.environ['DATABASE_URL'] and raises
      # ImproperlyConfigured exception if not found
      #
      # The db() method is an alias for db_url().
      'default': env.db(),

      # read os.environ['SQLITE_URL']
      'extra': env.db_url(
          'SQLITE_URL',
          default='sqlite:////tmp/my-tmp-sqlite.db'
      )
  }

  CACHES = {
      # Read os.environ['CACHE_URL'] and raises
      # ImproperlyConfigured exception if not found.
      #
      # The cache() method is an alias for cache_url().
      'default': env.cache(),

      # read os.environ['REDIS_URL']
      'redis': env.cache_url('REDIS_URL')
  }
  ```

## 09. url 작성
- 처음 요청이 들어오면 urls에서 맞는 경로로 분배해준다.
- app 안에 있는 views를 import
- urlpatterns 작성
  ```python
  from django.contrib import admin
  from django.urls import path
  from articles import views

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('index/', views.index, name='index'),
  ]
  ```
- Variabl Routing(변수 넣기)
  - \<path_converter:variable_name\>
  ```python
  path('articles/<int:num>/', views.hello)
  ```
  - converter는 str, int, slug, uuid, path 5종류. 선언안하면 기본으로 str이 됨.
- URL mapping
  - 여러 개의 app이 존재 할 때 하나의 urls.py에서 관리하지 않고 각 앱 폴더에 urls.py를 만들어 맵핑
  ```python
  from django.urls import path, include

  urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls'))
  ]
  ```
  ```python
  # articles/urls.py
  from django.urls import path
  from . import views

  app_name = 'articles'
  urlpatterns = [
      path('index/', views.index, name='index'),
      path('dinner/', views.dinner, name='dinner'),
  ]
  ```
- 이름 지정
  ```python
  app_name = 'articles' # 앱 이름
  urlpatterns = [
      path('index/', views.index, name='index'),  # url 이름
      path('dinner/', views.dinner, name='dinner'),
  ]
  ```
  ```django html
  {% url 'index' %}
  {% url 'articles:index' %}
  ```

## 10. view 작성

## 11. templates/앱이름 폴더 생성

## 12. template 작성
- template 상속

## 13. 

## 98. git 초기화시 주의사항
- .gitignore 작성
  - gitignore.io에서 파일 생성

## 99. 디버깅 정리
- 