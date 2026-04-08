## 목표

- Wireshark를 이용하여 PDF 파일 다운로드 패킷 캡처
- HTTP 상태 코드 분석

### 1. Wireshark 실행 및 캡처 시작

wifi를 사용 중이므로 해당 인터페이스를 선택하고 캡처를 시작하였다.

### 2. 디스플레이 필터 설정

HTTP 패킷만 보기 위해 필터를 설정하였다.

### 3. 사이트 접속 및 암호화 해제

HTTPS를 HTTP로 변경하여 패킷이 보이도록 하였다.

### 4. PDF 파일 다운로드

<img width="2879" height="1707" alt="Image" src="https://github.com/user-attachments/assets/0e92791c-42df-4a66-b662-1fd9aae4c0e1" />

### 5. 상태 코드 분석

<img width="1803" height="1268" alt="Image" src="https://github.com/user-attachments/assets/b76d97d7-1ea1-4fcc-975d-7e90c9bc5457" /><br>

- 패킷 구성 (총 174개)<br>
- 요청(Request): 87개<br>
- 응답(Response): 87개<br>
  : 요청과 응답의 개수가 1:1로 정확히 일치한다. 모든 요청에 대해 누락 없이 응답이 이루어졌음을 알 수 있다.<br><br>

- 요청 메서드(Method)<br>
- GET (75개)<br>
- POST (12개)<br><br>

- 응답 상태(Status)<br>
- 200 OK (87개): 모든 응답이 성공함! <br><br>

- 오류(4xx, 5xx): 0개. 통신 과정에서 발생한 에러나 거절된 요청이 없음.
