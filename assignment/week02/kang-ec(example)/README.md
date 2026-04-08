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
다운로드 과정에서 경고창이 발생하였고, 계속 버튼을 눌러 진행하였다.
사진을 보면 pdf 파일이 잘 다운받아진 것을 확인할 수 있다.
<img width="1662" height="1163" alt="image" src="https://github.com/user-attachments/assets/606c5789-8cce-4032-9f09-fa869d85f5d7" />


### 5. 상태 코드 분석  
<img width="1076" height="257" alt="image" src="https://github.com/user-attachments/assets/aa2cbacd-b71c-41c2-a2ec-492375b83240" />
- 2xx: 정상 응답 (200 OK) 209개<br>
- 3xx, 4xx, 5xx: 오류 없음 <br><br>

또한 HTTP는 포트 80을 사용하는 것을 확인하였다.
