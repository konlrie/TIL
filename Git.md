# Git 기초

> Git은 분산형버전관리시스템(DVCS)이다.(Shift + >)
>
> 소스코드의 이력을 확인하고, 협업 단계에서 활용 가능하다.

## 0. 기본 설정

윈도우에서 git을 활용하기 위해서는 git bash가 필요하다.[설치링크](https://gitforwindows.org/)

설치 이후에 commit을 작성하는 author 설정이 필요하다.

```bash
$ git gonfig --global user.name {github username}
$ git config --global user.email {github email}
$ git gonfig --global user.name konlpyrie@gmail.com
$ git config --global user.email konlrie
```

설정 내용을 확인하기 위해서는 아래의 명령어를 입력한다.

```bash
$ git config --global -l
user.email=konlpyrie@gmail.com
user.name=konlrie
```

## 로컬 저장소에서 활용하기

### 1. git 저장소 설정

특정 프로젝트 폴더에서 `git`을 활용하기 위해서는 아래의 명령어를 입력한다.

```bash
$ git init
Initialized empty Git repository in
C:/Users/student/Desktop/git/.git/
(master) $
```

* 해당 디렉토리 내에 `.git` 이라는 숨김 폴더가 생성되며, 모든 `git`과 관련된 동작은 해당 폴더에 기록된다.
* git bash에서 `(master)` 라는 브랜치 정보가 표기된다.

### 2. add

`git`에서 커밋할 대상 파일을 `staging area`로 이동시키는 명령어이다.

```bash
$ git add a.txt # 특정 파일을 stage
$ git add images/ # 특정 폴더를 stage
$ git add . # 모든 디렉토리 파일 및 폴더를 stage
```

* `add` 전 상태

  ```bash
  # 엔터 탭 벡스페이스
  $ git status
  On branch master
  
  No commits yet
  
  Untracked files: # git 이력에 담기지 않은 파일 생성
    (use "git add <file>..." to include in what will be committed)
    # git add 명령어를 통해서 커밋될 곳에 추가해라
          a.txt
          b.txt
  
  nothing added to commit but untracked files present (use "git add" to track)
  
  ```

  

* `add` 후 상태

```bash
$ git status
On branch master

No commits yet

Changes to be committed: # 커밋될 변경 사항
  (use "git rm --cached <file>..." to unstage)
        new file:   a.txt

Untracked files: # 트래킹 되고 있지 않은 파일들
  (use "git add <file>..." to include in what will be committed)
        b.txt

```



**항상 `git status` 명령어를 통해 현재 상태를 확인 하는 것이 중요하다!!!!**

### 3. commit

git에서 이력을 남기기 위해서는 `commit`을 통해서 진행한다.

`commit`을 남길 때에는 항상 커밋 메시지를 작성한다.

메시지는 해당 이력에 대한 정보를 담는다.

```bash
$ git commit -m '커밋메시지'
$ git commit -m 'Add files'
[master (root-commit) ce526e4] Add files
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a.txt
 create mode 100644 b.txt

```

커밋 이력을 확인하기 위해서는 아래의 명령어를 활용한다.

```bash
$ git log
commit ce526e4dc915b64b65c40b79690442a92260c256 (HEAD -> master)
Author: konlrie <konlpyrie@gmail.com>
Date:   Mon Dec 9 14:27:17 2019 +0900

    Add files
$ git status
On branch master
nothing to commit, working tree clean

```

이후 변경 사항이 발생하게 된다면, add -> commit을 한다.

`add` : 커밋할 대상 파일 선정

`commit` : 이력의 확정(스냅샷을 찍는다.라고도 표현)

## 원격 저장소(remote repository) 활용하기

> 원격 저장소를 제공해주는 서비스는 다양하다.
>
> 우리는 github을 기준으로 활용해보겠다.

### 0. 기본 설정

Githyb에 비어 있는 저장소(repository) 생성

### 1. 원격 저장소 설정

```bash
$ git remote add origin https://~
```

원격 저장소(remote)를 `origin`이라는 이름으로 https://~로 설정한다.

아래의 명령어를 통해서 저장된 원격 저장소 목록을 확인할 수 있다.

```bash
$ git remote -v
origin  https://github.com/konlrie/gittest.git (fetch)
origin  https://github.com/konlrie/gittest.git (push)
```

혹시 잘못 설정되었다면 아래의 명령어를 통해 삭제 가능하다.

```bash
$ git remote rm origin
$ git remote -v
```

### 2. push

원격 저장소에 업로드 하기 위해서는 push 명령어가 필요하다.

```bash
$ git push origin master
```

`origin` 으로 설정된 원격 저장소에 `push` 한다.

이후에 변경된 사항(commit)이 발생하였을 때, `git push origin master` 명령어를 통해서 매번 업로드를 해줄 수 있다.









