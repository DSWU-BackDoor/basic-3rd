# 1. 드림핵 워게임 풀이


## 1-1. 워게임 분야
- SQL Injection
- URL 접근 제한 미흡 취약점


## 1-2. 사진
### 1-2-1. SQL Injection
<img width="500" alt="스크린샷 2026-05-21 122851" src="https://github.com/user-attachments/assets/84e9b345-63c6-4d1e-9d30-61a521020a52" />


### 1-2-2. URL 접근 제한 미흡 취약점
<img width="500" alt="스크린샷 2026-05-21 132136" src="https://github.com/user-attachments/assets/8f7b1a7e-07c9-497d-ab58-2deb4ee96caf" />



## 1-3. 풀이
### 1-3-1. SQL Injection
- https://dreamhack.io/wargame/challenges/24 에 접속하여 소스 파일 다운로드 후, 서버 접속
- 에디터에서 소스 코드 분석
- 사용자 입력으로 인해 취약점이 발생할 가능성이 있는 부분 찾기
- res = query_db(f'select * from users where userid="{userid}" and userpassword="{userpassword}"') 부분에서 userid 부분과 userpassword 부분을 쌍따옴표(")로 감싸고 있는데, 만약 userid 부분에 "와 --(주석)을 넣어서 userid 뒷 부분, 즉 userpassword 부분을 주석 처리하면 비밀번호를 알지 못해도 로그인 가능
- 소스 코드에서 userid는 admin으로 제시되었으므로 id 창에는 admin" --을, 비밀번호 창에는 아무거나 입력하고 로그인
- 로그인에 성공하면 Flag 값이 나오므로, 복사해서 정답 입력


### 1-3-2. URL 접근 제한 미흡 취약점
- 소스 파일 다운로드 후, 서버 접속
- 에디터에서 소스 코드 분석
- session_id = os.urandom(4).hex() 부분에서 관리자 세션 ID를 1바이트 16진수로 나타내고 있음 -> 관리자 세션의 경우의 수는 00 ~ ff로 총 256개
- 'admin': FLAG 부분을 보면 admin이라는 관리자 계정에 대한 비밀번호는 FLAG 값이기 때문에 비밀번호를 알아내서 로그인 불가 -> 로그인을 직접 하는 게 아니라 브라우저의 쿠키 값(sessionid)을 직접 변조하여 관리자로 로그인된 것처럼 속여야 함
- Application -> Cookies -> sessionid의 값을 00~ff 범위에서 무작위로 입력하거나(burte force) Console에서 자동화 스크립트를 입력하여 관리자 세션 ID 찾기
- 관리자 세션 ID가 sessionid 값에 들어가면 Flag 값이 나오므로, 복사해서 정답 입력



# 2. VirtualBox & Ubuntu 설치 후 스크린샷
<img width="450" alt="스크린샷 2026-05-21 165844" src="https://github.com/user-attachments/assets/386142f8-5c00-4273-9157-b051ba958706" />

