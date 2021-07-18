

<center><h1>Git과 GitHub 사용법</h1></center>



## 1. Git 사용법

> Git : 버전 관리를 통한 코드 관리 도구. Linus Benedict Torvalds가 만듬



### 1.1 Git 설치

* Git Bash 설치
  * https://git-scm.com/downloads



### 1.2 CLI(Command Line Interface)를 통한 Git 사용법

> Working directory를 지정하고, Local repository를 생성하고, Add, Commit을 통해 버전을 관리
>
> Working directory에서 작업을 진행하고, Staging area를 거치고, Local repository에 변경사항을 반영



#### 1.2.1 Local repository 관리

1. Git Bash 실행
2. `mkdir folder_name` : 현재 디렉터리(`C:/Users/user_name`)에 `study_note` 폴더 생성

3. `cd study_note` : `study_note` 디렉터리로 이동(change directory)
4. `git init` : 현재 디렉터리(`C:/Users/user_name/study_note`)를 working directory로 설정
   *  현재 디렉터리에 `.git` 폴더가 생성됨
   * `user_name@DESKTOP-2F581FA MINGW64 ~/study_note (master)`와 같이 `(master)`표시가 붙음



#### 1.2.2 Local repository 관리

1. ````
   git config --global user.email "you@example.com"
   git config --global user.name "Your Name"
   ````

   * 두 명령어를 통해서 email과 name을 설정

2. 버전관리 할 코드 파일들을 Working directory에 위치시킴

   * `touch How-to-use-Git-and-GitHub.md` : `How-to-use-Git-and-GitHub.md` 파일을 생성
     * 파일명에 띄어쓰기가 있는 경우, 파일명을 꼭 `"`으로 묶어주어야 함

   * `code` : Visual Studio Code 실행

     * `How-to-use-Git-and-GitHub.md` 파일을 열어서 코드 수정

     * `Ctrl + K V` : Open preview to the side

     * `Ctrl + S` : Save

   * `git diff` : Commit 되어있는 버전과 현재 Working area의 차이를 출력

     * `git diff --staged` Commit 되어있는 버전과 Staging area의 차이를 출력
     * `git diff [해쉬1] [해쉬2]` : 두 Commit 간의 차이를 출력
       * `git diff 0c14a2 041d32`
     * `git diff HEAD HEAD^` : 가장 최근 Commit과 직전 Commit의 차이를 출력
     * `git diff [branch1] [branch2]` : 두 Branch 간의 차이를 출력
       * `git diff feature/test origin/master`

3. `git add How-to-use-Git-and-GitHub.md` : Staging area에 해당 파일의 변경사항을 올림

   * Staging area에 올리는 파일은 신규/수정 파일일 수도 있고, **삭제된 파일**일 수도 있음

   * 따라서 이미 삭제된 파일의 경우라도, 삭제되었다는 사실을 반영하기 위해 `add` 해줘야 함

   * `git add .` : Working area의 모든 변경사항을 한번에 Staging area에 올리기
   * `git reset HEAD How-to-use-Git-and-GitHub.md` : add 했던거 취소

4. `git commit -m "First commit"` : Staging area에 입력된 변경사항을 Local repository에 반영

   * `First commit`이라는 메시지가 기록된 새로운 버전이 생성됨

   * 각 단계에서 `git status`를 자주 활용하면, 현재의 진행상태를 파악하는데에 도움이 됨
   * `get reset HEAD^` : Commit 한거 취소 (Staging area 에서도 unstaged 됨)

5. `git log --oneline` 또는 `git log`를 통해 Local repository에 잘 Commit 되었는지 확인



## 2. GitHub 사용법

> GitHub : Remote repository를 제공하는 Hosting service 중 하나. Linus가 만든건 아님



### 2.1 GitHub에 Remote repository 생성하기

1. GitHub 회원가입 및 로그인

   * https://github.com/에서 회원가입을 하고 **로그인**을 한다

2. GitHub에 Remote repository 생성

   * 우측 상단의 `+`에서 New repositories를 통해 Remote repository를 생성

     * Remote repository의 name을 설정

     * `https://github.com/pepze21/study-note.git`와 같이 remote repository의 URL을 얻음

### 2.2 Local repository와 Remote repository를 연결하기 

1. `git remote add [shorthand name of Remote repository] [URL of Remote repository]` : 현재 Local repository에서 사용할 Remote repository를 추가

   * `git remote add origin https://github.com/pepze21/study-note.git`
   * 하나의 Local repository에 여러 개의 Remote repository를 연결할 수 있음
   * 관습적으로 별명(shorthand name)에 origin을 많이 씀 (original, 원본의 의미)

   * URL을 대신 origin을 적음으로써, 더 쉽게 reference 할 수 있음
   * git remote` 또는 `git remote -v`를 통해 Remote repository 목록을 확인 가능



### 2.3 Pull, Push, Clone으로 버전관리

1. `git push [저장소별명] [브랜치이름]`
   	* `git push origin master` : Local의 master(branch)를 origin(remote repository)에 push하기
   	* 아마 로그인되어있지 않다면 로그인 하라는 창이 뜰 것임. 그럼 로그인하면 됨
   	* `git push -u origin master` : 처음 push할 때 upstream으로 설정하면 `git push`만 해도 push가 됨
2. `git pull [저장소별명] [브랜치이름]`
    * `git pull origin master` : origin에 있는 master branch를 pull하기(가져오기)
    * `git pull` == `git fetch` + `git merge`
    * Pull은 **Local에 history가 이미 있는 상태**에서 Remote repository의 수정상태를 반영하는 것
3. `git clone https://github.com/pepze21/study-note.git` : Clone 생성
   * Clone은 `git init` 직후, **아무것도 없는 상태**에서 Remote repository의 Clone을 생성

