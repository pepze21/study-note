

<center><h1>Git과 GitHub 사용법</h1></center>



## 1. Git 사용법

> Git : 버전 관리를 통한 코드 관리 도구



### 1.1 Git 설치

* Git Bash 설치
  * https://git-scm.com/downloads



### 1.2 CLI(Command Line Interface)를 통한 Git 사용법

> Working directory를 지정하고, Local repository를 생성하고, add, commit을 통해 버전을 관리
>
> Working directory에서 작업을 진행하고, Staging area를 거치고, Local repository에 변경사항을 반영



#### 1.2.1 Local repository 생성 및 관리

1. Git Bash 실행
2. `mkdir folder_name` : 현재 디렉터리(`C:/Users/user_name`)에 `study_note` 폴더 생성

3. `cd study_note` : `study_note` 디렉터리로 이동(change directory)
4. `git init` : 현재 디렉터리(`C:/Users/user_name/study_note`)를 working directory로 설정
   *  현재 디렉터리에 `.git` 폴더가 생성됨
   * `user_name@DESKTOP-2F581FA MINGW64 ~/study_note (master)`와 같이 `(master)`표시가 붙음

5. 버전관리 할 코드 파일들을 해당 폴더 위치시킴
   * `touch "Git과 GitHub 사용법.md"` : `Git과 GitHub 사용법.md` 파일을 생성
     * 파일명에 띄어쓰기가 있는 경우 꼭 `"`으로 묶어주어야함
   * `code` : Visual Studio Code 실행
     * `Git과 GitHub 사용법.md` 파일을 열어서 코드 작성
     * `Ctrl + K V` : Open preview to the side
     * `Ctrl + S` : Save
6.  `git add "Git과 GitHub 사용법.md"` : Staging area에 `Git과 GitHub 사용법.md` 파일의 변경사항을 올림
   * Staging area에 올리는 파일은 신규 파일일수도 있고, 수정된 파일일 수도 있고, **삭제된 파일**일 수도 있음
7. `git commit -m "First commit"` : Staging area에 입력된 변경사항을 Local repository에 반영
   * `First commit`이라는 메시지가 기록된 새로운 버전이 생성됨

