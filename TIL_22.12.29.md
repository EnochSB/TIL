# 협업
## GitHub Profile README
1. 프로필 폴더 만들고 READM.md 파일에 자기소개 작성
2. Git 버전 만들기
3. **중요** GitHub 원격저장소 만들기
    저장소 이름은 *GitHub username*이어야한다.

## Branch
> 독립적인 작업흐름을 만들고 관리
1. 브랜치 생성
    ```bash
    (master) $ git branch {branch name}
    ```
2. 브랜치 이동
    ```bash
    (master) $ git checkout {branch name}
    ```
    ```bash
    - (master) $ git checkout -b {branch name}: 브랜치를 생성하고 이동.
    ```
3. 브랜치 병합
    ```bash
    (master) $ git merge {branch name}
    ```
4. 브랜치 삭제
    ```bash
    (master) $ git branch -d {branch name}
    ```
5. 브랜치 목록
    ```bash
    (master) $ git branch
    ```

## Git Flow
> Branch를 활용한 협업 전략
### 기본원칙
1. master branch는 반드시 배포 가능한 상태여야 한다.
2. feature branch 는 각 기능의 의도를 알 수 있도록 작성한다.
3. Commit message는 매우 중요하며, 명확하게 작성한다.
4. **Pull Request(PR)를 통해 협업을 진행한다.**
5. 변경사항을 반영하고 싶다면 master branch에 병합한다.

![GitFlow](22.12.29/git-flow_overall_graph.png)

## Branch 병합 시나리오
> branch 병합에는 3가지 시나리오가 있다.
>   - fast-foward
>   - merge commit
>   - merge conflict
### fast-foward
- feature branch 생성 후 master에 변경 사항이 없는 경우.
- 병합했을 때 feature branch가 그대로 master가 된다.

### merge commit
- 서로 다른 commit을 병합할 때 **서로 다른 파일**에만 작업이 일어난 경우.
- git이 auto merging을 진행.

### merge conflict
- 서로 다른 commit을 병합할 때 **같은 파일의 동일한 부분**에 작업이 일어난 경우.
- auto merging을 못하고 충돌 메시지 발생.
- 표시된 정보에 따라 수정을 진행하고 직접 commit을 한다.

## GitHub Flow Model
### Shared Repository Model
> Repository owner에게 초대를 받아 해당 저장소에 대한 push 권한을 받아 활용하는 방식
1. 팀원을 초대해 collaborator에 등록. push 권한을 부여
2. 팀원의 초대 수락
3. Clone 이후 작업 환경 설정
4. feature branch를 생성해 독립적으로 작업.
5. commit하고 push한다.
6. PR(Pull Request)한다.
7. 리뷰하고 병합한다.
8. 병합이 완료되면 로컬에서는 병합된 branch 삭제 후 origin으로부터 pull.

### Fork & Pull Model
> 초대를 받지 않고 ropository를 fork한 후에 활용하는 방식
1. repository를 fork해 내 repository를 만든다.
2. fork해서 생성된 내 repository를 clone해 작업한다.
3. commit, push, PR한다.
4. 병합되었다면 새로 fork
