# Bandit 복습 및 풀이 write-up


## 1. Level 0 -> Level 1
<img width="400" alt="image1" src="https://github.com/user-attachments/assets/b936baf0-51a2-43bb-ae11-03d5249b4c1d" />


- Level 0의 호스트와 비밀번호가 기본적으로 주어졌음. ```whoami``` 명령어로 현재 계정이 bandit0인지 확인하고 ```hostname```으로 서버 이름을 확인한 후 ```pwd```로 현재 경로를 확인한 후 문제 풀이를 진행함

- ```ls``` 명령어를 통해 파일 목록 확인 후 readme 발견
- ```cat readme``` 로 파일 내용 출력



## 2. Level 1 -> Level 2
<img width="400" alt="image2" src="https://github.com/user-attachments/assets/df7b1461-ff57-4693-8c1f-08bd7d6e4667" />


- 비밀번호는 '-' 라는 파일에 저장되어 있음
- 처음에 ```cat "-"```, ```cat -```를 시도했지만, 옵션으로 인식되어 정상적으로 출력되지 않았음. 
- ```rm "-"```도 시도했지만 파일 이름이 "-"으로 리눅스 명령어 옵션처럼 생겨서 발생하는 문제로 생각됨.
- 해결 방법: 상대 경로 사용
- ```cat ./-``` 명령어를 통해 텍스트 파일 내용 출력 성공



## 3.  Level 2 -> Level 3
<img width="400" alt="image3" src="https://github.com/user-attachments/assets/b3dc24ff-44e4-4cfe-8edc-fc02fdd43c8a" />

- 파일 이름이 --spaces in this filename-- 형태로 공백이 포함되어 있음
- 처음에 ```cat --spaces\ in\ this\ filename--``` 시도했으나, 공백과 -- 때문에 옵션으로 인식되어 오류 발생. 
- 해결 방법: 파일 이름 전체를 따옴표로 감싸 파일 내용 출력
- ```cat "./--spaces in this filename--"``` 로 출력 성공



## 4. Level 3 -> Level 4
<img width="400" alt="image4" src="https://github.com/user-attachments/assets/bb1ff211-3205-492f-bdc9-16d28c831199" />


- inhere 디렉터리의 숨겨진 파일 형태로 존재
- ```ls```로는 아무것도 읽히지 않았고, ```ls -a``` 명령어를 통해 다시 시도한 결과 숨겨진 파일을 확인 (...Hiding-From_You)
- ```cat ...Hiding-From-You``` 로 파일 내용 출력



## 5. Level 4 -> Level 5
<img width="400" alt="image5" src="https://github.com/user-attachments/assets/da8f91ec-e5af-4151-876d-13477f16cf1f" />


- 여러 개의 파일 중 사람이 읽을 수 있는 파일 하나에 비밀번호 존재
- 처음에 ```ls```만으로는 어떤 파일인지 타입 확인이 어려웠음
- ```file ./*``` 명령어를 사용하여 파일 타입을 확인한 결과 대부분은 data 파일이었고, 하나만 ASCII text라고 표시됨을 확인
- -file07이 해당 파일임을 확인
- ``` cat ./-file07``` 로 파일 내용 출력
- 이 때 파일 이름이 '-'로 시작되어서 ```./```를 붙여 출력해야 함



## 6. Level 5 -> Level 6
<img width="400" alt="image6" src="https://github.com/user-attachments/assets/965a099f-4b31-4305-a240-14d737789ce0" />


- 여러 maybehere 디렉터리 중 조건에 맞는 파일을 찾아야 함 (사람이 읽을 수 있는 파일, 크기 1033바이트, 실행 불가)
- 처음에 ```ls```로 디렉터리 구조 확인했지만, 파일이 너무 많아 직접 찾기에 어려움을 겪음.
- ```find . -type f -size 1033c```명령어 사용하여 조건에 맞는 파일을 자동 탐색함
- ```./maybehere07/.file2``` 발견
- ```cat "./maybehere07/.file2"```로 비밀번호 출력
