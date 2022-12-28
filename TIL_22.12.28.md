# Git/GitHub

## 분산버전관리시스템: 로컬에서 버전을 기록하고 관리하게 해준다.
- 작업을 (add) commit
- 작업: 파일을 생성 수정 삭제
- git은 파일의 이 변경사항을 추적한다.

## GitHub도 버전을 관리한다.
- Push: 로컬 저장소의 버전을 원격저장소로 보낸다.
- Pull: 원격저장소의 버전을 로컬 저장소로 가져온다.

## GitHub 사용을 위한 명령어
- $ git remote add origin url
    - 원격저장소를 맵핑(원격 저장소를 추가해라. 오리진으로 url을)
- $ git remote rm origin
- $ git remote -v
    - 원격저장소 정보 확인(v: verbose 상세하게 설명)
- $ git push origin master
- $ git pull origin master
- $ git clone url
    - init을 하지 않아도 된다.

## 협업을 위한 GitHub
### 협업할 때 온라인 저장소의 버전이 업데이트 된 경우
- pull하지 않고서는 로컬의 버전을 push 할 수 없다.
- 서로 다른 파일의 버전이 다르면 pull 했을 때 merge commit을 통해 통합해준다.
- 서로 같은 파일의 버전이 다르면 pull 했을 때 merge conflict를 통해 통합해준다.

### gitignore
- .gitignore 파일을 생성하고 그곳에 GIT으로 관리하지 않을 목록을 기록하면 GIT이 해당 파일과 폴더를 관리하지 않는다.
- 파일명(a.txt), 폴더명/(user/), *.해당 확장자(*.pptx), 폴더명/파일명(user/b.txt)
- 이미 commit한 경우에는 ignore할수 있을까?
- NO. 처음부터 잘 설정. commit을 지울 수는 있지만 안하는게 좋기때문.
- https://gitignore.io/ 에서 일반적인 개발자들이 사용하는 gitignore파일을 제공해준다.