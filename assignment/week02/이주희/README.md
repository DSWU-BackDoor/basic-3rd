## 목표  
- Wireshark를 이용하여 PDF 파일 다운로드 패킷 캡처  
- HTTP 상태 코드 분석  

### 1. Wireshark 실행 및 캡처 시작  
wifi를 사용 중이므로 해당 인터페이스를 선택하고 캡처를 시작하였다.

### 2. 디스플레이 필터 설정
HTTP 패킷만 보기 위해 디스플레이 필터를 HTTP로 설정하였다.

### 3. 사이트 접속 및 암호화 해제  
HTTPS를 HTTP로 변경했다.

### 4. PDF 파일 다운로드 
다운로드 후에 표시 필터를 문자열로 설정하고 'pdf'를 입력하여 다운로드 받은 파일을 확인했다.
<img width="2880" height="1702" alt="Image" src="https://github.com/user-attachments/assets/c26d68b3-4f2d-4584-8cc1-7d26ae016b50" /> 

### 5. 상태 코드 분석  
<img width="1214" height="304" alt="Image" src="https://github.com/user-attachments/assets/01b8b6e2-956e-4c98-887b-f39c482e00ad" />
- 2xx: 정상 응답 (200 OK) 121개
- 3xx: 리다이렉션 발생 (304)  
- 4xx, 5xx: 오류 없음  

HTTP는 포트 80을 사용하는 것을 확인하였다.
