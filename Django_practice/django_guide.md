# 장고 개발 가이드
## 개발 환경
### 01. 가상환경 생성 / 활성화
```bash
# 생성
$ python -m venv venv

# 활성화
$ source venv/Scirpts/activate
# 소스 v/스크립트/액트
# deactive로 비활성화
```

### 02. django 설치
```bash
$ pip install Django
```

### 03. 의존성 파일 생성
```bash
$ pip freeze > requirements.txt
# 파이썬 프리즈 화살표
```

### 04. 프로젝트 생성
```bash
$ django-admin startproject pjtname .
# 장고-어드민 스타트프로젝트 프로젝트명 띄고 쩜(.)
```

### 05. 서버 실행 및 종료
```bash
$ python manage.py runserver
# 파이썬 매니지.py 런서버
```
- ctrl + C 로 끄기

### 06. 앱 생성
```bash
$ python manage.py startapp appnames
# 앱 이름은 복수형 권장
# 짧은 소문자. 숫자, 공백, 특수문자 포함하지 않게
```

### 07. 앱 등록
- 프로젝트 폴더 > settings.py > INSTALLED_APPS에 앱이름 작성
- 앱을 생성한 후에 등록(반대는 불가)
- local app, 3rd party app, 기본 django app 순서 권장

### 08. Secretkey 환경변수
- pip install django-environ
- manage.py가 있는 곳에 .env 파일 생성
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
  BASE_DIR = Path(__file__).resolve().parent.parent

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
## MTV 작성
### 01. url 작성
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

### 02. view 작성
- 함수 사이 간격은 2칸이 스타일 가이드
- 기본
  ```python
  def index(request):
      return render(request, 'articles/index.html')
  ```
- throw catch
  ```python
  def throw(request):
      return render(request, 'articles/throw.html')


  def catch(request):
      message = request.GET.get('message')
      content = {
          'message': message,
      }
      return render(request, 'articles/catch.html', content)
  ```
  - template에서 content 활용
  ```django
  {{ message }}
  ```
- Variable Routing
  ```python
  def number_print(request, number):
      content = {
          'number': number,
      }
      return render(request, 'articles/number_print.html', content)
  ```

### 03. templates/앱이름 폴더 생성
- 앱 폴더 내에 templates/앱이름 폴더 생성
- 다른 경로 추가 가능
  - 생성 후 settings.py에 경로 추가.
  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR / 'templates'],
          'APP_DIRS': True,
      },
  ]
  ```

### 04. template 작성
- views.py에서 지정한 경로와 이름에 맞게 생성
- template 상속
  1. base.html 생성
  2. base가 될 코드 작성
  3. 상속받는 템플릿이 작성할 공간 규정
    ```django
    {% block content %}
    {% endblock content %}
    ```
  4. 자식 탬플릿에서 상속 선언 & 코드 작성
    ```django
    {% extends 'articles/base.html' %}

    {% block content %}
    {% endblock content %}
    ```

### 05. model 작성
- 모델 클래스 작성
  ```python
  class Todo(models.Model):
      content = models.CharField(max_length=80)
  ```
  - class \<테이블이름\>(models.Model)
  - 변수 = models.필드명(인자)
- make migrations
  ```bash
  python manage.py makemigrations
  ```
- migrate
  ```bash
  python manage.py migrate
  ```
- 모델 필드 추가
  - models.py에 원하는 클래스 추가
  - migrations
  - default 값 추가(기존 데이터들이 추가되는 필드에 어떤 값을 가져야 하는지)
- 관리자 계정 생성
  ```bash
  python manage.py createsuperuser
  ```
  - email은 선택사항
  - 비밀번호 입력시 화면에는 출력안됨
  - auth_user에 계정 확인
- 관리자 페이지 모델 등록
  - app폴더 내에 admin.py
  - from .models import 모델명
  - admin.site.register(모델명)

## ORM


### 96. fixtures
- Django가 데이터베이스로 가져오는 방법을 알고 있는 데이터 모음
- dumpdata: 데이터베이스의 모든 데이터 출력, 여러 모델을 하나의 json 파일로 만들 수도 있다.
```bash
$ python manage.py dumpdata --indent 4 app_name1.ModelName1 app_name1.ModelName2 app_name2.ModelName3 > data.json
# indent는 들여쓰기를 추가. 4로 tab의 효과.
$ python manage.py dumpdata --indent 4 > data.json
# 모든 모델 한 번에
```
- loaddata: fixtures 데이터를 데이터베이스로 불러오기
```bash
$ python manage.py loaddata data1.json data2.json data3.json
```
- fixtures 경로
  - django는 설치된 모든 app의 디렉토리에서 fixtures 폴더 이후의 경로로 파일을 찾아 load
  - 거기도 없다면 settings.py의 FIXTURE_DIRS에 설정된 경로에서 찾는다.
  - 명령어에 경로를 명시할 수도 있다.
  ```bash
    $ python manage.py loaddata foo/bar/mydata.json
  ```
- loaddata 순서 주의: 모델 관계에 따라 순서 중요
- loaddata 시 encoding codec 에러
  1. dumpdata 시 추가 옵션
  ```bash
  $ python -Xutf8 manage.py dumpdata [생략]
  ```
  2. 메모장활용
    - 메모장으로 json 파일 열기
    - 다른 이름 저장
    - 인코딩을 UTF8로 선택 후 저장


### 97. 날짜표시
- settings.py의 LANGUAGE_COD와 TIME_ZONE변경(Internationalization)
  ```python
  LANGUAGE_CODE = 'ko-kr'

  TIME_ZONE = 'Asia/Seoul'
  ```


### 98. git 초기화시 주의사항
- .gitignore 작성
  - gitignore.io에서 파일 생성

### 99. 디버깅 정리
- 