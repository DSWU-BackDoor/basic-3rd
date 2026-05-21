# 과제

## Wireshark 심화

## 목표  
- Wireshark를 이용하여 PDF 파일 다운로드 패킷 캡처  
- HTTP 상태 코드 분석  

### 1. Wireshark 실행 및 캡처 시작  
관리자 권한으로 Wireshark를 실행하여 네트워크 카드에서 오가는 모든 raw 패킷을 캡처하게 만들었다.
사용 중인 인터페이스는 wifi이니 이를 선택하고 캡처를 시작하였다.

### 2. 디스플레이 필터 설정
HTTP 상태 코드 분석이니 만큼 HTTP 패킷만 보이게 필터를 설정하였다.

### 3. 사이트 접속 및 암호화 해제  
HTTPS를 HTTP로 변경하여 패킷이 보이도록 하였다.

### 4. PDF 파일 다운로드  
다운로드 과정에서 경고창이 발생하였고, 계속 버튼을 눌러 진행하였다.
<img width="2880" height="1704" alt="Image" src="https://github.com/user-attachments/assets/149e1a31-726d-412a-a6e5-828a5327c09b" />

### 5. 상태 코드 분석  
<img width="1604" height="978" alt="Image" src="https://github.com/user-attachments/assets/b8f5a9e2-ddfc-409f-9323-47c788afd6fe" />

- 2xx: 정상 응답 (200 OK)  
- 3xx: 리다이렉션 발생 (302)  
- 4xx, 5xx: 오류 없음  

총 4개의 응답 패킷을 확인할 수 있었으며,  
리다이렉션은 HTTP 전환 과정에서 발생한 것으로 보인다.

또한 HTTP는 포트 80을 사용하는 것을 확인할 수 있었다.