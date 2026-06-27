### 7주차 과제 수정
첫 제출 당시 Ubutu 환경에서 문제 파일을 다운받아 rao를 컴파일, 취약점 확인 후 get_shell 주소 확인 후, 페이로드를 작성하여 쉘 획득까지는 확인하였지만, 플래그 파일 자체를 확인하지 못했고 결론적으로 풀이에 실패하였다. 

선배님께 조언을 얻어 문제 풀이를 재진행하여 풀이에 성공하였다. 

## 1. 문제 분석
첫 풀이 당시에는 직접 rao.c 파일을 열어 소스코드를 분석했다. 소스코드 상에서 ```buf[0x28]```부분이 취약점이라 생각하였고, 이 지점에서 ```scanf```를 받을 때 입력 크기의 제한이 없기 때문에 버퍼 오버플로우(BOF) 가 발생할 수 있다고 생각하였다. 
버퍼 오버플로우 자체가 스택의 버퍼에서 발생하기 때문에, 직접 스택 구조를 볼 수 있으면 좋겠다고 생각하였다. 

선배님의 풀이를 참고하니 ```disas main```을 통해 구조를 파악하신 것을 확인할 수 있었다. 이 방법을 참고하여 스택의 구조를 분석해보았다. 

<img width="400" alt="Image" src="https://github.com/user-attachments/assets/cb2d1516-0df8-4289-9989-5dc9c7424dd9" />

세 번째 줄을 보면,  ```sub rsp,0x30``` 에서  gcc가 buf를 위해 스택에 0x30 공간을 할당한 것을 확인할 수 있다. 코드 상에서는 ```buf[0x28]```로 40바이트의 스택 버퍼를 선언하였는데 실제로는 0x30이 할당된 것이다. 
아홉번째 줄에 buf의 시작 주소를 확인해보면 ```lea rax,[rbp-0x30]```로 시작 주소가 rbp-0x30임을 확인할 수 있다. 

이어서 ```b *main +54```와 ```r``` 통해 브레이크포인트를 설정해 실행한다. scanf 호출 직전에 브레이크 포인트를 걸고, r로 실행하는 코드이다. 
(b: 특정 주소에 브레이크포인트를 설정, 도달하면 일시 정지)
<img width="400" alt="Image" src="https://github.com/user-attachments/assets/6837d221-7ca6-4e31-b095-9a329913bab5" />

실행 후 레지스터 부분을 확인해보면

```RSI 0x7fffffffe020``` : scanf의 두 번째 인자, buf의 주소
```RBP 0x7fffffffe050``` : 현재 함수의 베이스 포인터
```RSP 0x7fffffffe020 ``` : 스택 포인터

RSP(스택 포인터)가 RSI와 같은 이유는 ```sub rsp, 0x30```을 통해 buf에 0x30만큼의 공간을 주었기에 RSP가 buf의 시작 주소를 가리키게 된다. 
RBP(현재 함수의 베이스 포인터)의 경우 함수가 ```0x7ffffffffe020```에서 실행된 뒤(RSP), 버퍼에 ```sub rsp, 0x30```로 0x30만큼이 할당되었기 때문에 RSP보다 +0x30이 된 ```0x7fffffffe050```에 위치하게 된다. 

즉, 현재 함수의 베이스 포인터 RBP가 ```0x7fffffffe050```이면, 오버플로우를 발생시킬 버퍼는 버퍼의 크기인 0x30만큼, 즉 rbp-0x30인 ```0x7fffffffe20```부터 ```0x7fffffffe50```내에 위치한다. 


<img width="400" alt="Image" src="https://github.com/user-attachments/assets/5d2bfcae-9e87-4aaa-9fb6-12e13940862c" /> 

RBP에 스택 프레임 포인터(SFP)가 저장되고, scanf실행 전 상태이고, scanf 뒤에는 mov, leav, ret 순서로 실행, ret에서 리턴 주소로 점프한다. 

<img width="400" alt="Image" src="https://github.com/user-attachments/assets/2fee88b5-7f7a-48cc-a7b9-386379d75184" />

스택 부분의 마지막을 보면 rbp+0x8인 ```0x7fffffffe58```이  리턴주소이다. 

따라서 오프셋 전체는 0x30 + 0x08 = 0x38 = 56바이트
이기에 총 56 바이트를 뒤집어 씌우고, 리턴주소를 get_shell의 주소로 바꾸어야 한다. 


## 2. 실행 과정

rao.c를 확인해보면 셸을 실행해주는 get_shell()함수가 있다. 따라서 이 함수의 주소로 main 함수의 반환 주소를 덮어서 셸을 획득한다. 

```p get_shell```을 통해 주소를 확인한다. 확인 결과 주소는 ```0x4066aa```이다. 

<img width="400" alt="Image" src="https://github.com/user-attachments/assets/ff4be6bd-15f6-4c59-9423-363463273f3a" />


파악한 정보를 바탕으로 익스플로잇 코드를 작성한다. 파이썬 라이브러리인 pwn을 이용해 ```exploit.py```를 만든다. 

터미널에 ```gedit exploit.py```로 파일을 만들어 작성한다. 

<img width="200" alt="Image" src="https://github.com/user-attachments/assets/1ffa45a3-5bb4-40af-9199-4bd986f94966" />
<img width="400" alt="Image" src="https://github.com/user-attachments/assets/eb3d9f31-547e-4a18-a314-c7090ad878a5" />

사용중인 리눅스는 리틀엔디안을 사용한다. 따라서 페이로드를 프로그램에 전달할 때 엔디언을 적용해야 한다. 
이에 주소인 0x4006aa를 이에 맞게 변환해야 하는데 이 코드가 ```p64(0x4006aa)```이다. 

또한 dreamhack에서 생성한 VM 서버 포트를 통해 Exploit 코드에 연결해야하며, 이를 위한 코드가 ```p = remote('host3.dreamhack.games', 11034)```이다. 

페이로드 구성은 ```b'A' * 0x30 + b'B' * 0x8  + p64```로 다음과 같다. 
```A *0x30``` : buf 채우기
```B *0x08``` : RBP 저장
```0x4006aa``` : 리턴 주소


작성한 익스플로잇 코드를 실행한다. 이 과정에서 내 로컬 터미널이 아닌, 서버 쉘로 접속해야 한다. 

<img width="400" alt="Image" src="https://github.com/user-attachments/assets/11f187ce-2c10-4577-915b-c6e7c80dd3ae" />

id를 입력했을 때 사용자 이름이 rao로 뜨고, 서버 쉘에 접속되었다는 뜻이다. 

<img width="400" alt="Image" src="https://github.com/user-attachments/assets/d7948994-9735-4396-a4bb-9205658014bc" />

```ls```를 입력해 파일 목록에서 flag 파일을 찾았다. 이후 flag 파일을 ```cat flag```를 통해 읽어 플래그를 확인하였다. 

<img width="400" alt="Image" src="https://github.com/user-attachments/assets/0480a1a8-978d-4cc4-a803-47ecade8e7d8" />


## 3. 결론 및 고찰 
우선, 첫 번째 풀이 때 막혔던 부분은, dreamhack의 VM이 실행되지 않았고, 따라서 flag 획득이 어려웠던 것이다. 내 로컬 Ubuntu에서 파일을 직접 읽어 실행하다보니 다른 부분은 잘 진행되었지만 서버 쉘로의 접속이 어려웠다. 과제를 다시 풀이하면서 익스플로잇 코드 작성 시 생성한 VM 서버 포트를 연결하는 방법을 통해 해결할 수 있었다. 
exploit 코드를 작성하는 방식에서도 기존에는 gedit을 사용하지 않았는데, gedit을 사용해 직접 exploit 파일을 만드니 조금 더 깔끔하고 편리하게 풀이를 할 수 있었다. 
