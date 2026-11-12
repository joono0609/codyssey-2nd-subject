## 프로젝트 개요

Python 을 이용하여 터미널에서 동작하는 퀴즈게임을 개발하고 객체지향 프로그램 이해 와  Git 과 GitHub 를 활용하여 협업 하기 위한 프로젝트

### 퀴즈 주제 및 선정 이유

* Python 은 인공지능에서 가장 널리 사용하는 프로그램언어로 이 언어의 기본 명령어를 잘 습득하고자 인공지능을 이용하여 문제를 선정했음

### 실행 환경

| 항목 | 내용 |
| --- | --- |
| Python 버전 | 3.11.6 |
| 인코딩 | UTF-8 |
| Git |2.56.0.windows.4 |
| 실행 커맨드 | `python main.py` |

### 실행 방법
```
cd /Users/user/2st_subject
python main.py
```

### 파일 구조

```
2nd-subject/
├─ main.py          # 주 프로그램
├─ state.json       # 저장된 퀴즈 + 최고 점수 + 기록
├─ .gitignore 
└─ README.md
```

### 기능 목록 및 화면

* 퀴즈 목록 표시

<img width="537" height="402" alt="image" src="https://github.com/user-attachments/assets/e371704b-0867-4fd4-bc50-4ed0c360785c" />

* 퀴즈 풀기

<img width="537" height="642" alt="image" src="https://github.com/user-attachments/assets/2f1f09f3-2253-4984-a54d-28f056210775" />
<img width="537" height="492" alt="image" src="https://github.com/user-attachments/assets/b5af15d2-b985-4acc-9f69-22b2b1c889bd" />

* 퀴즈 추가

<img width="535" height="351" alt="image" src="https://github.com/user-attachments/assets/6be9ba34-203e-4a10-ba94-cce45402f135" />

* 퀴즈 목록 표시

<img width="536" height="366" alt="image" src="https://github.com/user-attachments/assets/4709f497-0d17-4507-b1b4-df2b99d4c031" />

* 점수 확인

<img width="537" height="197" alt="image" src="https://github.com/user-attachments/assets/d1ba3868-6299-41e8-966a-faf068dda9b4" />

* 종료

<img width="537" height="195" alt="image" src="https://github.com/user-attachments/assets/e1ea7975-d1b3-4999-ab4e-cbd38c91af5b" />

git log --oneline --graph 결과

<img width="1215" height="626" alt="image" src="https://github.com/user-attachments/assets/d4f23f6a-077f-4368-bdf1-b4f65900061e" />

branch 및 merge 로그 
```
PS C:\Users\user\2st_subject> git checkout -b dev-main
Switched to a new branch 'dev-main'

PS C:\Users\user\2st_subject> git status
On branch dev-main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        __pycache__/
        test.py

main.py 수정 후 저장

git status 

PS C:\Users\user\2st_subject> git status
On branch dev-main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   main.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        __pycache__/
        test.py

git add main.py
git commit -m "dev-main 브랜치 생성하고 퀴즈풀기 관련기능 추가 반영 "

PS C:\Users\user\2st_subject> git checkout main
M       main.py
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
PS C:\Users\user\2st_subject> git merge dev-main
Already up to date.

PS C:\Users\user\2st_subject> git checkout dev-main
M       main.py
Switched to branch 'dev-main'
PS C:\Users\user\2st_subject> git status
On branch dev-main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   main.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        __pycache__/
        test.py

PS C:\Users\user\2st_subject> git commit -m "dev-main 브랜치 생성하고 퀴즈풀기 관련기능 추가 반영 "
[dev-main 8fc5139] dev-main 브랜치 생성하고 퀴즈풀기 관련기능 추가 반영
 1 file changed, 35 insertions(+), 4 deletions(-)
PS C:\Users\user\2st_subject>
PS C:\Users\user\2st_subject> git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
PS C:\Users\user\2st_subject> git merge dev-main
Updating 3837250..8fc5139
Fast-forward
 main.py | 39 +++++++++++++++++++++++++++++++++++----
 1 file changed, 35 insertions(+), 4 deletions(-)
```
