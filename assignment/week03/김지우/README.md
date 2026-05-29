# 1. 기본 분석

- 사용된 프로토콜을 3가지 이상 작성하시오.
1) HTTP: 웹 통신을 위한 프로토콜로, 클라이언트와 서버 간 요청 및 응답에 사용됨
2) TCP: 신뢰성 있는 데이터 전송을 위한 전송 계층 프로토콜
3) IP: 패킷의 주소 지정 및 라우팅을 담당하는 네트워크 계층 프로토콜


# 2. 웹 요청 분석

<img width="1557" height="1579" alt="Image" src="https://github.com/user-attachments/assets/0115e1bb-fdcb-4fe5-8c93-2bdfe94fe79b" />

- HTTP 요청 중 ".pdf" 파일을 다운로드하는 요청을 찾으시오.

GET /ebook/src/viewer/m2/img/movieplay.png HTTP/1.1

- 전체 URL (http:// 포함)을 작성하시오.

http://www.yongin.go.kr/ebook/src/viewer/download.php?host=main&site=20220430_101634_1&no=1

- 요청 방식(GET/POST)을 작성하시오.

GET


# 3. 서버 응답 분석

<img width="1613" height="1579" alt="Image" src="https://github.com/user-attachments/assets/9b0a7135-3c66-4a5e-8659-28e4290982fa" />

- 서버가 반환한 파일의 종류는 무엇인가?

application/pdf

- 파일 크기는 얼마인가?

867700 bytes

- 파일 이름은 무엇인가?

(23)_도시계획_계획의_실행.pdf


# 4. 파일 복구

-  NetworkMiner를 사용하여 파일을 복구하고, 복구 과정을 단계별로 작성하시오.
-  복구 과정 화면을 캡처하여 첨부하시오.

<img width="1914" height="1593" alt="Image" src="https://github.com/user-attachments/assets/8ab6610d-4ad3-44a8-8fc4-c441e77c38e6" />


우선 과제 파일이 .pcgpng 형태였기 때문에 파일을 다운로드받아 wireshark-관리자모드로 열었다. 개인 노트북을 사용하여 Wi-Fi를 선택하여 시작했다.


<img width="1903" height="633" alt="Image" src="https://github.com/user-attachments/assets/be5c379f-219e-48fe-bc63-190d0134647b" />


NetworkMiner를 통해 분석하기 위해서는 .pcap형태의 파일이 필요하기 때문에 다운로드받은 과제 파일의 형식을 변환해 '3주차과제'라는 제목으로 다시 저장하였다. 



<img width="1600" height="1148" alt="Image" src="https://github.com/user-attachments/assets/d2e47b59-0f91-44d0-a377-13a645885e9f" />


NetworkMiner에서 '3주차과제' 파일을 오픈하면 다음과 같은 화면이 뜬다. 



<img width="1601" height="1145" alt="Image" src="https://github.com/user-attachments/assets/7d98822a-211e-4f7c-ba5c-4476f0d0e878" />
<img width="2879" height="1799" alt="Image" src="https://github.com/user-attachments/assets/55660eb2-2952-4102-b55d-c46783136fcc" />


상단의 바에서 Files로 들어가고, pdf를 검색하면 다운로드했던 pdf파일을 찾을 수 있다. 이 파일을 다시 다운로드 하면 복구 성공이다.
