# 1. 기본 분석

- HTTP, TCP, DNS


# 2. 웹 요청 분석

- HTTP 요청 중 ".pdf" 파일을 다운로드하는 요청을 찾으시오.

- 전체 URL (http:// 포함)을 작성하시오.
http://www.yongin.go.kr/ebook/home/view.php?host=main&site=20220430_101634_1&listPageNow=0&list2PageNow=0&code=12&code2=0&code3=0&optionlisttype=L&listcount=10&searchcode=0&searchcode2=0&searchdate=0&searchkey=&searchval=&searchandor=&dummy=&&orders=

- 요청 방식(GET/POST)을 작성하시오.
GET /ebook/src/viewer/download.php?host=main&site=20220430_101634_1&no=1 HTTP/1.1

- 서버가 반환한 파일의 종류는 무엇인가? 
application/pdf

- 파일 크기는 얼마인가? 
867700

- 파일 이름은 무엇인가?
%2823%29_%EB%8F%84%EC%8B%9C%EA%B3%84%ED%9A%8D_%EA%B3%84%ED%9A%8D%EC%9D%98_%EC%8B%A4%ED%96%89.pdf

# 4. 파일 복구

-  NetworkMiner를 사용하여 파일을 복구하고, 복구 과정을 단계별로 작성하시오.
1. pcap 로드
<img width="933" height="437" alt="Image" src="https://github.com/user-attachments/assets/cc0636de-fee1-454c-b326-41cb141567d2" />
2. files 탭으로 이동
<img width="995" height="531" alt="Image" src="https://github.com/user-attachments/assets/ba71c0b4-52ea-418b-bb42-891f20e57a1b" />
3. 대상 탐색
<img width="991" height="545" alt="Image" src="https://github.com/user-attachments/assets/eb1eaba5-3779-4b07-b83e-1bd862ca9cd1" />
4. 파일 복구
<img width="992" height="537" alt="Image" src="https://github.com/user-attachments/assets/3b96c129-7c03-4177-84ba-b9dfe1d86462" />