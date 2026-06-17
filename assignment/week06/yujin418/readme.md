week06 과제 제출창입니다.
# 사전 지식
1. 리눅스 파일 시스템 탐색의 기본
리눅스는 CLI(명령줄 인터페이스) 환경이기 때문에, 마우스 없이 명령어로만 폴더를 이동하고 파일을 확인해야 합니다.

ls (List): 현재 디렉터리(폴더)에 있는 파일과 폴더 목록을 보여줍니다.

ls -a: 숨겨진 파일(파일명이 .으로 시작하는 파일)까지 모두 보여줍니다.

ls -l: 파일의 상세 정보(권한, 크기, 수정 날짜 등)를 리스트 형태로 보여줍니다. (보통 합쳐서 ls -al을 가장 많이 씁니다.)

cd (Change Directory): 디렉터리를 이동합니다.

cd ..: 상위(이전) 폴더로 이동

cd ~: 홈 디렉터리(로그인했을 때 첫 위치)로 이동

cat (Concatenate): 파일의 내용을 터미널 화면에 그대로 출력해 주는 명령어입니다.

2. 특수 문자가 포함된 파일 다루기 (레벨 1~2 핵심)
리눅스 터미널에서 공백(Space)이나 대시(-)는 고유의 기능을 가진 특수 문자입니다. 파일 이름에 이들이 포함되어 있다면 리눅스가 오해하지 않도록 명시해 주어야 합니다.

공백(Space)이 있는 파일
터미널에서 공백은 명령어와 인자(Argument)를 구분하는 기준입니다.

해결책: 파일 이름을 작은따옴표(' ')나 큰따옴표(" ")로 감싸거나, 공백 앞에 역슬래시(\ )를 붙여 일반 문자로 인식시킵니다.

예시: cat 'spaces in this filename' 또는 cat spaces\ in\ this\ filename

대시(-)로 시작하는 파일
리눅스 명령어 뒤에 붙는 대시(- 또는 --)는 주로 '옵션'을 뜻합니다. (예: ls -al에서 -al)

해결책: 파일 이름 앞에 상대 경로인 ./ (현재 디렉터리라는 뜻)를 붙여서, 문장의 시작이 대시가 아니게 만들어야 합니다.

예시: cat ./-file 또는 cat "./--spaces in this filename--"

3. 숨겨진 파일과 사람이 읽을 수 있는 파일 (레벨 3~5 핵심)
앞으로 마주하게 될 레벨들에서 요긴하게 쓰일 사전 지식입니다.

숨겨진 파일 (Hidden Files)
리눅스에서 파일 이름이 점(.)으로 시작하는 파일(예: .passwd)은 숨김 파일로 처리되어 일반 ls 명령어로는 보이지 않습니다.

해결책: 반드시 ls -a 또는 ls -al 명령어를 사용해 확인해야 합니다.

파일의 종류 확인하기 (file 명령어)
리눅스에서는 확장자(예: .txt, .exe)가 없어도 파일 이름만 마음대로 바꿀 수 있습니다. 겉보기엔 텍스트 파일 같아도 실제로는 실행 파일이거나 압축 파일일 수 있습니다.

사용법: file [파일명]

출력 예시: ASCII text라고 나오면 사람이 읽을 수 있는 텍스트 파일이 맞고, data라고 나오면 컴퓨터만 읽을 수 있는 이진(Binary) 데이터 파일입니다.

# Bandit 복습 및 풀이 write-up


## 1. Level 0
<img width="678" height="548" alt="Image" src="https://github.com/user-attachments/assets/9dd51db3-3f78-4544-b2ef-cc96fd268e18" />
<img width="637" height="593" alt="Image" src="https://github.com/user-attachments/assets/d3e19ccd-8928-43a8-b1f7-9f44ebb7fb51" />

- Level 0의 호스트와 비밀번호는 기본적으로 주어짐
- ```ssh -p 2220 bandit0@bandit.labs.overthewire.org```를 입력하고 비밀번호인 bandit0을 입력하여 로그인


## 2. Level 0 -> Level 1
<img width="695" height="277" alt="Image" src="https://github.com/user-attachments/assets/3e5dede4-9c67-435c-963b-8bc85c851aff" />
<img width="878" height="353" alt="Image" src="https://github.com/user-attachments/assets/c6247086-5d31-4c93-b12e-84951fe201ef" />

- 다음 비밀번호는 bandit0 계정의 홈 디렉터리에 있는 readme 파일에 저장되어 있음
- ```ls``` 명령어를 통해 디렉터리 안에 readme가 있는지 확인
- ```cat``` 명령어를 통해 텍스트 파일 내용(비밀번호) 출력
- ```exit``` 명령어를 통해 접속 종료 후 bandit1 계정에 찾은 비밀번호를 이용하여 접속


## 3. Level 1 -> Level 2
<img width="883" height="202" alt="Image" src="https://github.com/user-attachments/assets/1c60c37e-7695-4cf0-8104-0eaba279c339" />
<img width="880" height="362" alt="Image" src="https://github.com/user-attachments/assets/3647c4b0-3b0f-4986-9e12-89cc2650a35d" />

- 비밀번호는 bandit1 계정의 홈 디렉터리에 있는 '-' 라는 파일에 저장되어 있음
- '-'로 시작하는 파일 이름은 리눅스 명령어 옵션(-h, -f 등)과 이름이 겹쳐 충돌이 발생
- 명령어 뒤에 --를 붙이거나 상대 경로로 표현해야 함
- ```cat -- -``` 또는 ```cat ./-``` 명령어를 통해 텍스트 파일 내용 출력
- ```exit``` 명령어를 통해 접속 종료 후 bandit2 계정에 찾은 비밀번호를 이용하여 접속


## 4. Level 2 -> Level 3
<img width="877" height="332" alt="Image" src="https://github.com/user-attachments/assets/95337bd3-60e8-45d5-8c1e-6ab1db4ea536" />
<img width="855" height="351" alt="Image" src="https://github.com/user-attachments/assets/0ebef5ca-4ae1-4a7c-a083-435ff5ce8e9d" />

- 비밀번호는 bandit2 계정의 --spaces in this filename-- 홈 디렉터리에 있는 파일에 저장되어 있음
- 공백이 있는 파일이름의 경우 파일 전체를 큰따옴표(") 또는 작은 따옴표(')를 이용해 감싸줘서 표현해야 함
- ```cat "./--spaces in this filename--"``` 명령어를 통해 텍스트 파일 내용 출력
- ```exit``` 명령어를 통해 접속 종료 후 bandit3 계정에 찾은 비밀번호를 이용하여 접속


## 5. Level 3 -> Level 4
<img width="863" height="233" alt="Image" src="https://github.com/user-attachments/assets/ec14e83e-aeda-4dd0-a2f6-22edab378e04" />
<img width="882" height="362" alt="Image" src="https://github.com/user-attachments/assets/acaf7164-42b9-4bf1-8a87-5ad433369070" />
- 비밀번호는 bandit3 계정의 inhere 디렉터리의 숨겨진 파일에 저장되어 있음
- 숨겨진 파일까지 확인하기 위해서는 ```ls -al(또는 ls -a)``` 명령어를 통해 확인
- ```ls -al``` 명령어 통해 숨겨진 파일 ...Hiding-From-You 확인
- ```cat ...Hiding-From-You``` 명령어를 통해 텍스트 파일 내용 출력
- ```exit``` 명령어를 통해 접속 종료 후 bandit4 계정에 찾은 비밀번호를 이용하여 접속


## 6. Level 4 -> Level 5
<img width="838" height="227" alt="Image" src="https://github.com/user-attachments/assets/3b1e264d-fe41-40ee-ae5e-255ab6e977d7" />
<img width="816" height="356" alt="Image" src="https://github.com/user-attachments/assets/23ac8de7-320f-4a7a-a5bc-46ade2fa5984" />
- 비밀번호는 bandit4 계정의 inhere 디렉터리에 있는 유일하게 사람이 읽을 수 있는 파일에 저장되어 있음
- ```file ./*``` 명령어를 입력하면 해당 파일이 어떤 형태인지 확인 가능
- 결과에 ASCII text라고 표시되는 파일이 유일하게 사람이 읽을 수 있는 파일
- -file07이 유일하게 ASCII text라고 표시됨
- ``` cat ./-file07``` 명령어를 통해 텍스트 파일 내용 출력
- ```exit``` 명령어를 통해 접속 종료 후 bandit5 계정에 찾은 비밀번호를 이용하여 접속
