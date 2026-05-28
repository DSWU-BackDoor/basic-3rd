# Bandit 복습 및 풀이 write-up


## 1. Level 0
<img width="400" alt="스크린샷 2026-05-28 180727" src="https://github.com/user-attachments/assets/77212bcd-8a25-4e45-94f2-9a2eac0b36ab" />
<img width="400" alt="스크린샷 2026-05-28 180750" src="https://github.com/user-attachments/assets/44b0a9aa-d551-4551-90e7-25e0a633a6ec" />

- Level 0의 호스트와 비밀번호는 기본적으로 주어짐
- ```ssh -p 2220 bandit0@bandit.labs.overthewire.org```를 입력하고 비밀번호인 bandit0을 입력하여 로그인


## 2. Level 0 -> Level 1
<img width="400" alt="스크린샷 2026-05-28 180811" src="https://github.com/user-attachments/assets/814137cb-1af2-4880-85e4-66602d54dd6e" />
<img width="1774" height="1141" alt="스크린샷 2026-05-28 180831" src="https://github.com/user-attachments/assets/a79dd53e-306d-429c-806b-333b66b2f21c" />

- 다음 비밀번호는 bandit0 계정의 홈 디렉터리에 있는 readme 파일에 저장되어 있음
- ```ls``` 명령어를 통해 디렉터리 안에 readme가 있는지 확인
- ```cat``` 명령어를 통해 텍스트 파일 내용(비밀번호) 출력
- ```exit``` 명령어를 통해 접속 종료 후 bandit1 계정에 찾은 비밀번호를 이용하여 접속


## 3. Level 1 -> Level 2
<img width="400" alt="스크린샷 2026-05-28 180850" src="https://github.com/user-attachments/assets/d582eabd-4266-4fd0-9187-88261d757572" />
<img width="400" alt="스크린샷 2026-05-28 180911" src="https://github.com/user-attachments/assets/a8367774-fb01-4c33-a1b9-d9af6dbac1ca" />

- 비밀번호는 bandit1 계정의 홈 디렉터리에 있는 '-' 라는 파일에 저장되어 있음
- '-'로 시작하는 파일 이름은 리눅스 명령어 옵션(-h, -f 등)과 이름이 겹쳐 충돌이 발생
- 명령어 뒤에 --를 붙이거나 상대 경로로 표현해야 함
- ```cat -- -``` 또는 ```cat ./-``` 명령어를 통해 텍스트 파일 내용 출력
- ```exit``` 명령어를 통해 접속 종료 후 bandit2 계정에 찾은 비밀번호를 이용하여 접속


## 4. Level 2 -> Level 3
<img width="400" alt="스크린샷 2026-05-28 180930" src="https://github.com/user-attachments/assets/e3b41c55-2c65-4de1-821b-26ffa2ecec12" />
<img width="400" alt="스크린샷 2026-05-28 180947" src="https://github.com/user-attachments/assets/cad57650-f457-4da9-862c-0dc5ca0cc35d" />

- 비밀번호는 bandit2 계정의 --spaces in this filename-- 홈 디렉터리에 있는 파일에 저장되어 있음
- 공백이 있는 파일이름의 경우 파일 전체를 큰따옴표(") 또는 작은 따옴표(')를 이용해 감싸줘서 표현해야 함
- ```cat "./--spaces in this filename--"``` 명령어를 통해 텍스트 파일 내용 출력
- ```exit``` 명령어를 통해 접속 종료 후 bandit3 계정에 찾은 비밀번호를 이용하여 접속


## 5. Level 3 -> Level 4
<img width="400" alt="스크린샷 2026-05-28 181011" src="https://github.com/user-attachments/assets/0f345201-fa2f-4dde-ac5b-8929c316b96b" />
<img width="400" alt="스크린샷 2026-05-28 181029" src="https://github.com/user-attachments/assets/81375150-7484-42c5-89b5-c08dc4cea7ef" />
<img width="400" alt="스크린샷 2026-05-28 181045" src="https://github.com/user-attachments/assets/ed1aa651-0bc7-4dbb-a2d9-608c86c69627" />

- 비밀번호는 bandit3 계정의 inhere 디렉터리의 숨겨진 파일에 저장되어 있음
- 숨겨진 파일까지 확인하기 위해서는 ```ls -al(또는 ls -a)``` 명령어를 통해 확인
- ```ls -al``` 명령어 통해 숨겨진 파일 ...Hiding-From-You 확인
- ```cat ...Hiding-From-You``` 명령어를 통해 텍스트 파일 내용 출력
- ```exit``` 명령어를 통해 접속 종료 후 bandit4 계정에 찾은 비밀번호를 이용하여 접속


## 6. Level 4 -> Level 5
<img width="400" alt="스크린샷 2026-05-28 181120" src="https://github.com/user-attachments/assets/bc15b329-a66c-45df-9c77-04ff8a1a84f7" />
<img width="400" alt="스크린샷 2026-05-28 181139" src="https://github.com/user-attachments/assets/e19774d2-1142-4296-a10f-d50136d8235a" />

- 비밀번호는 bandit4 계정의 inhere 디렉터리에 있는 유일하게 사람이 읽을 수 있는 파일에 저장되어 있음
- ```file ./*``` 명령어를 입력하면 해당 파일이 어떤 형태인지 확인 가능
- 결과에 ASCII text라고 표시되는 파일이 유일하게 사람이 읽을 수 있는 파일
- -file07이 유일하게 ASCII text라고 표시됨
- ``` cat ./-file07``` 명령어를 통해 텍스트 파일 내용 출력
- ```exit``` 명령어를 통해 접속 종료 후 bandit5 계정에 찾은 비밀번호를 이용하여 접속
