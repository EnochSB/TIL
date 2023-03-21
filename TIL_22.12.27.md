# Git/GitHub
## 목표
1. Markdown을 활용한 문서작성
2. Git을 활용한 버전 관리
    - 버전 관리 기본
    - Git branch
    - Git: 소스코드를 관리하는 프로그램
    - GitHub: Git의 온라인 플랫폼
    - Git을 통해 포트폴리오를 구성할 수 있다.
3. GitHub를 활용한 포트폴리오 관리 및 개발 프로젝트 시나리오
    - 개인 포트폴리오 관리
    - 프로젝트(협업)

## Markdown 기반 문서 작성
### 워드프로세서와의 차이점
- 텍스트 기반의 마크업 언어(html의 ml이 markup language)
    - 문서를 구조화 할 수 있는 기능이 있는 언어가 마크업 언어.
- 단순한 텍스트 문법으로 내용을 작성하며, 다양한 환경에서 변환하여 보여짐.
- README.md로 파일 이름을 만들어 공식문서 등에 활용

### 정적사이트생성기(Static site generator) 기반 블로그
Jekyll, Gatsby, Hugo, Hexo 등으로 작성된 마크다운을 HTML, CSS, JS파일 등으로 변환하고 깃허브 페지 기능을 통해 기록 가능.

### 마크다운 기반 SW
Jupyter notebook에는 별도의 마크다운 셀으로 프로젝트 내용과 분석 결과를 정리 가능함
Notion과 같은 메모/노트 필기 소프트웨어도 마크다운 기반 문서 작성을 기본으로 함.

# 마크다운 문법 정리

## 제목(Heading)
- #의 개수로 소제목 구분(#, ##, ###, ...)

## 리스트(List)
- ol: 순서가 있는 리스트(-, *)
- ul: 순서가 없는 리스트(1, 2, 3 ...)
    - tab으로 하위 항목 구성.

## Fenced Code block
- backtick(`) 기호 3개로 코드를 작성 가능 (```)
- \```python으로 파이썬 코드 작성 시작
    ```python
    print('Hello python')
    #주석
- \```html으로 html 코드 작성 시작
    ```html
    <!-- 주석 -->
## Inline Code block
- 특정 단어를 코드블록으로 사용
- backtick 기호 사이에 \`코드블록\` -> `코드블록`

## Link
- \[문자열](url)을 통해 링크 작성
- ex) \[구글](https://google.com) -> [구글](https://google.com)

## 이미지
- \!\[이미지이름](이미지주소)를 통해 이미지 삽입

## 인용문
- \>로 작성
> 인용문

## 테이블
- |로 작성

>\| Syntax | Description |
>
>\| ----------- | ----------- |
>
>\| Header | Title |
>
>\| Paragraph | Text |

>| Syntax | Description |
>| ----------- | ----------- |
>| Header | Title |
>| Paragraph | Text |

## 텍스트 강조
- 굵게(\*\*문자\*\*), 기울임(\*문자\*), 취소선(\~~문자~~)

## 수평선
- \---로 작성
---

- 가운데정렬, 색바꾸기, 이미지 크기 조정 등은 마크다운에서는 불가능.
- 마크다운 기반의 소프트웨어에서 제공하면 사용.

## CLI
### CLI 환경과 GUI 환경의 차이점
- CLI 환경에서 기초 파일 시스템 조작
- CLI(Command Line Interface): 명령어 인터페이스.가상 터미널 또는 텍스트 터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식.
- interface: 사용자의 이용을 위한 접면
- CLI를 사용할 때는 현재 열려있는 위치를 알아야한다.

### 명령어
- ls: 리스트
- mkdir: 디렉토리 생성 make directory
- cd 폴더명: 디렉토리 이동 change directory
- cd ..: 상위 디렉토리 이동
- .: 현재 디렉토리
- ..: 상위디렉토리
- touch 파일명: 파일 생성
- rm 파일명: 파일 삭제 remove
- rm -r 폴더명: -r을 넣어 재귀적으로 폴더 안에까지 삭제해야 폴더 삭제 가능
- pwd: 현재 디렉토리 출력 print working directory

# 버전 관리의 의미
- GIT: 분산 버전 관리 시스템
    - 버전 업데이트를 할때마다 각 버전의 모든 소스코드를 각각 백업해놓을까?

## Git 명령어
- $ git init: 로컬 저장소 생성
- $ git add {file}
    - working directory상의 변경 내용을 staging area에 기록
    - staging area: 버전으로 기록하기 위한 파일 변경사항의 목록
- $ git commit -m {커밋메시지}
    - staged 상태의 파일들을 커밋을 통해 버전으로 기록
- $ git log(커밋 기록 조회)
    - $ git log -- oneline
    - $ git log -- oneline --graph
- $ git status(파일 변경 상태)
- 사용자 정보 입력
    - $ git config --global user.name "username"
    - $ git config --global user.emal "my@emai.com"
- 사용자 정보 확인
    - $ git config -l
    - $ git config --global -l
    - $ git config user.name
- $ git restore --staged {file}
    - add한 파일을 staging area에서 지우기
- $ git restore {file}
    - working directory상의 변경 내용을 취소하고 최신 커밋으로 되돌린다.
