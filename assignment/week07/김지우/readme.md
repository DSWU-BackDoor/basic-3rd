## 1. 문제 분석
<img width="400" alt="Image" src="https://github.com/user-attachments/assets/d71a704c-0d9f-4928-b65f-58da04fce04e" />

<img width="400" alt="Image" src="https://github.com/user-attachments/assets/e429b403-7d6c-457d-9f85-bad2ac947c97" />

-드림핵 사이트에서 제공하는 가상머신을 이용하려 하였으나, 실행이 되지 않아 ubuntu 환경에서 문제 파일을 다운로드 받고, 압축을 푼 후, 터미널에서 진행하였다. 

<img width="916" height="260" alt="Image" src="https://github.com/user-attachments/assets/9c017899-07ac-4659-874d-a68b67cd9166" />

-바이너리 실행 시 입력을 받는 구조였고, 취약점은 gets 또는 scanf 입력으로 인한 버퍼 오버플로우(BOF)였다. 

## 2. 실행 과정

<img width="902" height="70" alt="Image" src="https://github.com/user-attachments/assets/33d0d4b2-937e-4193-8c37-923cd0b79b28" />

- rao.c 파일을 확인해보면 셀을 실행해주는 get_shell() 함수가 작성되어있다. 이에 gbd를 통해 ```p get_shell```의 주소를 확인하였다. 이 주소로  

- 페이로드 구성은 다음과 같이 하였다. 

A * 0x30 → buffer overflow
B * 0x8 → saved RBP overwrite
0x4011dd → return address overwrite

- 페이로드를 엔디언을 적용해서 프로그램에 전달하는 과정이다. ```0x4011dd```가 메모리에 어떻게 저장되는지는 visual studio 를 통해 직접 확인해 보았다. 
<img width="1098" height="354" alt="Image" src="https://github.com/user-attachments/assets/e2348ebc-123a-48f6-b327-493371e19cd4" />
<img width="400" alt="Image" src="https://github.com/user-attachments/assets/d20574bc-e825-4d9b-900c-94031522c432" />

이를 통해 ```g0x4011dd```는 ```"\xdd\x11\x40\x00\x00\x00\x00\x00"```으로 전달되어야 함을 확인하였고, 이를 바탕으로 엔디언을 적용하여 익스플로잇을 작성하였다.
<img width="400" alt="Image" src="https://github.com/user-attachments/assets/fc7dbd26-efc4-4419-aaf0-18467764dec0" />

## 3. 결론 및 아쉬운 점
- 버퍼 오버플로우 취약점을 이용하여 페이로드를 통해 return address(RIP)를 덮는 데 성공하였다. 이를 통해 프로그램의 실행 흐름이 특정 함수로 변경되는 것을 확인하였다. 그러나 해당 함수가 flag를 출력하는 함수가 아니었기 때문에 최종적으로 flag를 획득하지는 못하였다.