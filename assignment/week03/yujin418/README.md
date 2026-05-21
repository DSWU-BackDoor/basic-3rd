# 1. 기본 분석

- HTTP, TCP, DNS


# 2. 웹 요청 분석

- HTTP 요청 중 ".pdf" 파일을 다운로드하는 요청을 찾으시오.

- 전체 URL (http:// 포함)을 작성하시오.
http://www.yongin.go.kr/ebook/home/view.php?host=main&site=20250410_095137&listPageNow=0&list2PageNow=0&code=15&code2=0&code3=0&optionlisttype=L&listcount=10&searchcode=0&searchcode2=0&searchdate=0&searchkey=&searchval=&searchandor=&dummy=&&orders=

- 요청 방식(GET/POST)을 작성하시오.
GET /ebook/src/viewer/download.php?host=main&site=20250410_095137&no=1 HTTP/1.1
25_용인생활가이드북_웹용_0409.pdf

# 3. 서버 응답 분석

- 서버가 반환한 파일의 종류는 무엇인가? 
application/pdf

- 파일 크기는 얼마인가? 
25433559

- 파일 이름은 무엇인가?
25_%EC%9A%A9%EC%9D%B8%EC%83%9D%ED%99%9C%EA%B0%80%EC%9D%B4%EB%93%9C%EB%B6%81_%EC%9B%B9%EC%9A%A9_0409.pdf

# 4. 파일 복구

-  NetworkMiner를 사용하여 파일을 복구하고, 복구 과정을 단계별로 작성하시오.
1. pcap 로드
<img width="982" height="604" alt="Image" src="https://github.com/user-attachments/assets/ad4b25f3-060e-452a-9982-356ac50df579" />
2. files 탭으로 이동
<img width="988" height="534" alt="Image" src="https://github.com/user-attachments/assets/5a4395db-c9f4-49bc-8e95-9bbfd28c228d" />
3. 대상 탐색
<img width="982" height="518" alt="Image" src="https://github.com/user-attachments/assets/5466e4f6-aa6e-4fe7-aafe-dc32428c4af5" />
4. 파일 복구
<img width="914" height="912" alt="Image" src="https://github.com/user-attachments/assets/9381b779-cfef-475c-917f-2782f5feae09" />

-  복구 과정 화면을 캡처하여 첨부하시오.
