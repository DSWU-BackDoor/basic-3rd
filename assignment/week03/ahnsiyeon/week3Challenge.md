# 1. 기본 분석

- 사용된 프로토콜을 3가지 이상 작성하시오.
TCP(Transmission Control Protocol), HTTP(Hypertext Transfer Protocol), DNS(Domain Name System)

# 2. 웹 요청 분석

- HTTP 요청 중 ".pdf" 파일을 다운로드하는 요청을 찾으시오.
GET /ebook/src/viewer/download.php?host=main&site=20220430_101634_1&no=1 HTTP/1.1 

- 전체 URL (http:// 포함)을 작성하시오.
http://www.yongin.go.kr/ebook/src/viewer/download.php?host=main&site=20220430_101634_1&no=1

- 요청 방식(GET/POST)을 작성하시오.
get

# 3. 서버 응답 분석

- 서버가 반환한 파일의 종류는 무엇인가?
pdf

- 파일 크기는 얼마인가?
867700 B

- 파일 이름은 무엇인가?
도시계획_계획의_실행

# 4. 파일 복구

-  NetworkMiner를 사용하여 파일을 복구하고, 복구 과정을 단계별로 작성하시오.

Wireshark에서 패킷 캡쳐 파일을 .pcap 형태로 저장
NetworkMiner에서 파일 열기
확장자가 pdf인 항목 찾기
해당 파일 우클릭 후 Open File

-  복구 과정 화면을 캡처하여 첨부하시오.
![alt text](image.png)