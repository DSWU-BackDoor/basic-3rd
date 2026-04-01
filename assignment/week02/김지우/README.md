# Wireshark 심화

## 목표
- Wireshark를 이용하여 PDF 파일 다운로드 패킷 캡처
- HTTP 상태 코드 분석


### 실습 과정

**1. Wireshark 실행**
관리자 권한으로 실행한다.


**2. 패킷 캡처 시작**
WIFI를 선택하여 시작하였다. 


**3. 디스플레이 필터에 `HTTP` 설정**
<img width="1135" height="956" alt="Image" src="https://github.com/user-attachments/assets/acaee386-91cd-478a-91d3-6d078847fca3" />

Wireshark 상단 북마크 표시를 눌러 필터를 HTTP로 설정해 주었다.


**4. 용인시 홈페이지 접속** 
HTTPS로 설정되어 있는 홈페이지 주소를 HTTP로 바꾸어 암호화를 해제하였다. 


**5. 홈페이지에서 PDF 파일 다운로드**  
<img width="1437" height="1177" alt="Image" src="https://github.com/user-attachments/assets/5c79e795-b669-4035-b6c1-8c3056461817" />

HTTP 상태에서 PDF 다운로드를 할 경우 경고창이 뜨고, 계속 버튼을 눌러 진행한다. 

<img width="2879" height="1799" alt="Image" src="https://github.com/user-attachments/assets/24c736a9-03ad-4e19-a07a-51c62b5cee07" />

다운로드 완료 이후 Wireshark 창에서 'Ctrl+F'를 누르고 문자열을 검색한다. 'pdf'를 찾아 검색하면 정상적으로 다운로드가 완료되었을 경우 사진처럼 'application/pdf'라는 문구가 확인된다.


**6. 패킷 캡처 종료 후 저장**



### 분석 내용
<img width="2879" height="1799" alt="Image" src="https://github.com/user-attachments/assets/e76bf2aa-470a-4288-bd16-c9be8b172bb5" />

2xx: Success
200 OK

정상응답 59개

3xx: Redirection
304 Not Modified

Wireshark를 이용하여 PDF 다운로드 과정의 패킷을 분석하던 중 HTTP 응답 코드 304 Not Modified를 확인하였다. 찾아보니 해당 코드는 클라이언트가 이전에 캐시에 저장된 파일의 변경 여부를 서버에 요청한 결과, 파일이 수정되지 않았음을 의미한다. 이 경우 서버는 실제 PDF 데이터를 다시 전송하지 않고, 클라이언트는 기존에 저장된 파일을 그대로 사용하게 된다.
수업 중 실습에서는 해당 응답이 관찰되지 않았으나, 이후 개인 실습 과정에서 나타난 것으로 보아 동일한 파일을 반복 요청하는 상황에서 캐싱 메커니즘이 동작한 것으로 해석된다. 이를 통해 HTTP 통신에서 캐싱이 네트워크 효율성에 중요한 역할을 한다는 점을 확인할 수 있었다.

5xx: Server Error
4xx: Client Error
1xx: Informational

위 세 개에 대해서는 오류가 발생하지 않았다. 


---
