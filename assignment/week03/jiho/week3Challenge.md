# 1. 기본 분석

- 사용된 프로토콜을 3가지 이상 작성하시오.
tcp, http, dns

# 2. 웹 요청 분석

- HTTP 요청 중 ".pdf" 파일을 다운로드하는 요청을 찾으시오.
: 요청 확인 완료
- 전체 URL (http:// 포함)을 작성하시오.
: http://www.yongin.go.kr/ebook/src/viewer/download.php?host=main&site=20220430_101634_1&no=1
- 요청 방식(GET/POST)을 작성하시오.
: GET을 사용함
# 3. 서버 응답 분석

- 서버가 반환한 파일의 종류는 무엇인가?
: pdf 파일
- 파일 크기는 얼마인가?
: 867700
- 파일 이름은 무엇인가?
: (23)_도시계획_계획의_실행.pdf

# 4. 파일 복구

-  NetworkMiner를 사용하여 파일을 복구하고, 복구 과정을 단계별로 작성하시오.

1. 우선 저장한 pcapng 파일을 pcap로 변환한다(wireshark 활용)
2. networkminer로 분석 시작
3. files 탭 선택
4. 파일 목록 확인
4. 파일 우클릭 이후 open 선택, 이후 열람 가능

-  복구 과정 화면을 캡처하여 첨부하시오.
<img width="1002" height="551" alt="Image" src="https://github.com/user-attachments/assets/7cf36fe8-1fe5-45ef-a4ac-fc89f4a939c1" />

<img width="1003" height="553" alt="Image" src="https://github.com/user-attachments/assets/7e8ed1d0-88f2-4021-a66d-3eba712e72b2" />

<img width="1001" height="705" alt="Image" src="https://github.com/user-attachments/assets/e8f63165-c5a1-41e1-b303-17ad00275580" />

<img width="952" height="1020" alt="Image" src="https://github.com/user-attachments/assets/27444c1c-2000-4cde-88f9-d054dbee5ba7" />