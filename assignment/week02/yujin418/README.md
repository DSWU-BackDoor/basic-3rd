# 과제
- week02 파일 안에 본인 이름 파일을 만든 후 그 안에 제출.

## Wireshark 심화

### 목표
- Wireshark를 이용하여 PDF 파일 다운로드 패킷 캡처
- HTTP 상태 코드 분석

### 제출 방법
아래 구조를 따라 GitHub에 업로드<br>
week02/<br>
&nbsp; └ 본인이름/<br>
&nbsp;&nbsp;    ├ README.md<br>
&nbsp;&nbsp;    └ capture.pcapng<br>

### 제출 파일
- Wireshark 패킷 캡처 파일 (`.pcapng`)
- 결과 정리 파일 (`.md` 또는 `.txt`)<br>
 ※ README 작성 시 **와이어샤크 환경에서 pdf 다운 받은 패킷이 캡처된 화면 첨부 필수**<br>
 ※ 패킷 캡처 화면, 상태 코드 확인 화면 등의 **스크린샷 첨부를 권장**

### 실습 과정
1. Wireshark 실행
2. 패킷 캡처 시작
3. 디스플레이 필터에 `HTTP` 설정
4. 용인시 홈페이지 접속  
 (https → http로 변경하여 암호화 해제)
5. 홈페이지에서 PDF 파일 다운로드  
 (다운로드 전체 과정 패킷 캡처)
 - http 환경에서는 경고창이 뜨면 "계속" 클릭
6. 패킷 캡처 종료 후 저장

### 분석 내용
- `통계 → HTTP → Packet Counter → HTTP Response Packets`
- 주요 상태 코드(200, 301, 404 등) 확인 및 의미 간단히 정리

---

# 결과 작성

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

### 5. 상태 코드 분석  
- 2xx: 정상 응답 (200 OK)  
- 3xx: 리다이렉션 발생 (304 Not Modified)  
- 4xx, 5xx: 오류 없음  

총 77개의 응답 패킷을 확인할 수 있었으며,  
리다이렉션은 브라우저 캐시에 이미 동일한 파일이 존재하여 서버가 데이터를 재전송하지 않고 로컬 데이터를 사용하도록 안내한 결과로 보임

또한 HTTP는 포트 80, HTTPS는 포트 443을 사용하는 것을 확인하였다.

패킷 캡쳐 화면 zip
[capture.pcapng.gz](https://github.com/user-attachments/files/26328991/capture.pcapng.gz)