# ssafy 서울 7반 알고리즘 스터디 2팀
### 바로가기
- [📢 RULES](#📢-rules)
- [ℹ️ 코드 업로드 방식](#ℹ️-코드-업로드-방식)
- [📁 폴더 구조](#📁-폴더-구조)
- [ℹ️ Commit Convention](#ℹ️-commit-convention)
- [ℹ️ PR 방법](#ℹ️-pr-방법)
- [ℹ️ 이슈 작성 방법](#ℹ️-이슈-작성-방법)
- [브랜치 작성 방법](#branch-작성법)
- [💻 문제 목록](#💻-문제-목록)

## ** 절대로 메인 레포지토리에서 푸쉬를 하지마 **
## (중요) 커밋 전 포크받은 레포지토리의 sync 버튼 클릭 후 pull 받아주세요~~~~

## 📢 RULES
- 평일 하루 1문제, 주말 하루 3문제 이상 풀기. 
- 풀지 못한 문제라도 코드리뷰를 위해 올려주세요. ( 내 힘으로 풀고싶다면 사전에 양해 구해주세요. )
- 본인 조 OR 다른 조라도 PR 확인 후 코드리뷰 작성하기.
- 중간에 막히는 부분이 있어 질문하고 싶으면 이슈 적극 활용하기
- 반드시 fork 후 본인의 레포지토리에서 사용한다.
- 자기 폴더를 제외한 다른 폴더를 건드리지 않는다. ( 병합 과정에서 오류가 발생할 수 있음 )
- 하루 해야할것 : 문제풀이 , 조원 코드 리뷰
- 절대로 직접 PR을 승인하지 말것.

## 💻 문제 목록
- 04.03
    - IM 문제 : [백준 : 덩치](https://www.acmicpc.net/problem/7568)
    - A형 문제 : [백준 : 뿌요뿌요](https://www.acmicpc.net/problem/11559)
- 04.04
    - IM 문제
        - [백준 : 수열](https://www.acmicpc.net/problem/2559)
        - [백준 : 체스판 다시 칠하기](https://www.acmicpc.net/problem/1018)
    - A형 문제 : [백준 : 낚시왕](https://www.acmicpc.net/problem/17143)
## ℹ️ 코드 업로드 방식
1. 메인 레포지토리를 FORK 하고 clone 한다. (최초 1회)
2. 문제사이트/문제번호 로 구성된 Branch를 생성한다. (ex: BOJ/1123)
    - [브랜치 작성 방법](#branch-작성법) 참고
2. 폴더 구조와 커밋 컨벤션에 맞춰 업로드 한다.
    - [📁 폴더 구조 ](#📁-폴더-구조) 참고
    - [ℹ️ Commit Convention](#ℹ️-commit-convention) 참고
3. 메인 레포지토리로 PULL REQUEST를 올린다.
    - [ℹ️ PR 방법](#ℹ️-pr-방법) 참고
4. 코드리뷰 2개 이상 달릴시 메인 레포지토리에 머지 됨.
## 📁 폴더 구조 
아래 양식에 따라 디렉토리 생성 생성해주세요!
- `본인이름 / 문제 사이트 / 문제 번호`
- `BOJ`: 백준
- `SWEA`: SWEA
- `PGM`: 프로그래머스
- `※ input 파일은 들어가지 않습니다. ※`

### 예시
```
📦seunghoon
 ┣ 📂BOJ
 ┃ ┣ 📂1125
 ┃ ┃ ┗ 📜sol.py
 ┃ ┗ 📂1592
 ┃ ┃ ┗ 📜sol.py
 ┗ 📂SWEA
```



## ℹ️ Commit convention
### title
- `[Commit Type] : message `
- `Commit Type`
    - 문제 해결 완료: `[Solve]`
    - 문제 미해결: `[Fail]`
    - 코드 수정: `[Fix]`
    - 코드 최적화: `[Refactor]`
    - 문서 작업: `[Docs]`

- `예시`
    - [Solve] :문제이름 문제 해결
    - [Fail] : 문제이름 문제 시간초과로 실패
    - [Fix] :문제이름 문제 오타 수정
    - [Refactor] : 문제이름 문제 코드 함수화
    - [Docs] : README.md 추가 내용 추가

### body
- 구조
```
'''
[문제 사이트트] - 문제 이름

문제풀이 세부 내용
'''
```
- `문제 사이트`
    - [BOJ]
    - [SWEA]
    - ...
### 최종 메세지 예시  
- 문제 해결시
```
[Solve] : 문제이름 문제 해결

[BOJ] 1234:
    - 문제 유형 : BFS
    - 문제 난이도 : 백준 골드 3
    - 시간복잡도 : 23ms
    - 공간복잡도 : 1000mb
```

- 문제 해결 실패시
```
[Fail] : 문제이름 문제 런타임 에러로 해결 실패

[BOJ] 1234:
    - 문제 유형 : BFS
    - 문제 난이도 : 백준 골드 3
    - 재귀 깊이 런타임 에러로로 인해 실패
```

- 풀이 수정시
```
[Fix] : 문제이름 문제 오타 수정

[BOJ] 1234:
    - printt(a) => print(a) 오타 수정정

```

- 코드 리팩토링시
```
[Refactor] : 문제이름 문제 

[BOJ] 1234:
    - 함수 단일 책임 원칙에 따른 더하기, 찾기 로직 분리

---
```


## ℹ️ PR 방법
### 1. 메인 레포지토리에서 FORK 버튼 클릭
![alt text](/README_ASSETS/image.png)

### 2. 레포지토리 경로 설정 후 Create Fork 클릭
![alt text](/README_ASSETS/image-1.png)

### 3. 문제 커밋 진행 후, 상단의 Pull Requests 클릭 후 new pull request 버튼 클릭
![alt text](/README_ASSETS/image-2.png)

### 4. 경로 확인(중요) 후 create pull request 버튼 클릭
![alt text](/README_ASSETS/image-3.png)

### 5. 내용 작성
- 제목 : [문제 사이트] - 문제 번호 + 메세지
- 내용 : 문제 링크, 풀이 코드, 풀이 방법 설명
- 예시
> ```
> # [BOJ] 1054
> [문제 이름](문제 url)
>
> ## 문제 코드
> '''python
> print('test')
> '''
> 
> ## 풀이 방식
> - 프린트함
> ```

### 6. reviewr , assigness, label 설정 
- reviewr에 팀장과 자기 조원들 추가
- 자기 PR에 맞는 라벨 추가
- 스터디장 assigness에 추가
![alt text](/README_ASSETS/image-4.png)

### 7. 이후 Create Pull Request 버튼 클릭!



## ℹ️ 이슈 작성 방법
### 1. 이슈 버튼 클릭
![alt text](/README_ASSETS/issue.png)

### 2. 이슈 작성
- 제목 : [문제 사이트] - 문제 번호 + 메세지
- 내용 : 자유 형식이되 코드를 같이 붙여 넣어주세요!
![alt text](/README_ASSETS/issue2.png)

### 3. assigness 설정
- 도와줄 스터디원들 + 자기 자신 assigness 설정해주세요.
- ![alt text](/README_ASSETS/issue3.png)

### 4. label 설정
- 자기가 작성한 리뷰에 맞는 라벨링을 진행해 주세요!
![alt text](/README_ASSETS/issue4.png)

### 이후 create 하면 완료!


## Branch 작성법
### - 문제풀이 작성하기 이전에 진행해 주세요!!
### 브랜치란 ? 
- git 에서 코드를 분기하여 관리하는 개념.
- 예시 이미지
![alt text](/README_ASSETS/branch.png)

### 사용하는 이유?
\#14 이슈 참고
 - 간단요약
    - PR시 문제 1을 커밋, 푸쉬하고 PR을 올린다. 
    - 이후 문제 2를 커밋, 푸쉬하면 기존 문제1 PR에 같이 올라간다.
    - 이를 해결하기 위해 branch 를 이용한다. 

### 진행 방법
1. 터미널을 킨다.

2. 현재 브랜치가 master인 경우
    1. git pull을 받는다.
        - `$ git pull`
    2. git checkout -b 문제사이트/문제번호(BOJ/1102) 명령어로 브랜치 생성 -> 이동한다. 
        - `$ git checkout -b BOJ/1123`
        - (주의) 반드시 모든 커밋이 이미 진행된 상태에서 진행해야 합니다. `git status`시 아무것도 없어야함.
    3. 터미널에 master가 브랜치명 (BOJ/1123) 로 바뀐걸 확인한다.
    4. 문제파일 생성 후 커밋 진행한다.
    5. git push origin 브랜치명 을 통해 push 한다.
        - `$ git push origin 브랜치명(BOJ/1123)`
    6. github에서 PR 진행한다.


2. 현재 브랜치가 다른곳인 경우
    1. git checkout master로 마스터 브랜치로 복귀한다. (이때 이전 브랜치에 모든 commit이 진행되어 있어야 한다.)
        - `$ git status` : 아무것도 없어야함.
        - `$ git checkout master` : 마스터 브랜치로 이동
    2. git pull을 통해 레포지토리에 있는 정보를 가져온다.
        - `$ git pull`
    3. git checkout -b 브랜치명을 통해 브랜치 생성 후 이동한다.
        - `$ git checkout -b BOJ/1153`
    4. 파일 생성 및 코드 작성 후 커밋 진행한다.
        - `$ git add .` 
        - `$ git commit -m ~~~~~`
    5. 레포지토리에 푸쉬를 진행한다.
        - `$git push origin BOJ/1153`
    6. github에서 pr 진행한다.

### 추가 참고자료
1. [뉴비를 위한 Github 브랜치 참고자료](https://sseozytank.tistory.com/107)
2. [github 명령어 모음(살짝 틀린부분 있을수도 있음)](https://velog.io/@develeep/TILgit-%EB%AA%85%EB%A0%B9%EC%96%B4)