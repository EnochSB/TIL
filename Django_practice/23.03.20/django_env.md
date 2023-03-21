# 장고 개발 환경 설정 가이드
## 01. 가상환경 생성 / 활성화
```bash
# 생성
python -m venv venv

# 활성화
source venv/Scirpts/activate
# 소스 v/스크립트/액트
```

## 02. django 설치
```bash
pip install django==3.2.18
# 3.2.18 = 최신버전
```

## 03. 의존성 파일 생성
```bash
python freeze > requirements.txt
# 파이썬 프리즈 화살표
```

## 04. 프로젝트 생성
```bash
django-admin startproject pjt .
# 장고-어드민 스타트프로젝트 프로젝트명 띄고 쩜(.)
```

## 05. 서버 실행
```bash
python manage.py runserver
# 파이썬 매니지.py 런서버
```
- ctrl + C 로 끄기

## 99. git 초기화시 주의사항
- .gitignore 작성
  - gitignore.io에서 파일 생성