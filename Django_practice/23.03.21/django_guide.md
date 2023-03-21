# 장고 개발 환경 설정 가이드
## 01. 가상환경 생성 / 활성화
```bash
# 생성
$ python -m venv venv

# 활성화
$ source venv/Scirpts/activate
# 소스 v/스크립트/액트
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

## 99. git 초기화시 주의사항
- .gitignore 작성
  - gitignore.io에서 파일 생성