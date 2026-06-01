week02_Wireshark실습


실습 순서 


(1) Wireshark 실행
관리자 권한으로 실행
노트북인 경우: ‘Wi-Fi’ / 실습실 컴퓨터인 경우: ‘이더넷 2’ 선택
더블 클릭 or 마우스 오른쪽 버튼 누르고 ‘캡처 시작’ 클릭

(2) 캡처 시작

(3) 디스플레이 필터에서 ‘HTTP’ 설정
디스플레이 필터 → 캡처한 패킷에서 원하는 패킷만 보여주도록 함

(4) 용인시 접속 → http://www.yongin.go.kr
사이트 암호화 제거 (패킷 캡처 가능하도록) https → http 로 변경
HTTPS를 HTTP로 변경하여 패킷이 보이도록 함

(5) 용인시 홈페이지 내 아무 pdf나 다운로드 (모든 과정을 전부 패킷 캡처 진행)
다운로드 과정에서 경고창이 발생해도 계속 버튼을 눌러 진행

(6) 패킷 캡처 종료 후 패킷 저장
기본 저장 형식 '.pcapng' 
'.pcap'으로도 저장 가능 (호환성 필요할 때)
저장 안 하고 종료하면 데이터 날아갈 수 있음

(7) 통계 - HTTP - 패킷 카운터 - HTTP Response Packets
→ 상태 코드 분석


실습 과정


pdf 다운로드 성공!!! 
<img width="1280" height="820" alt="week02-01" src="https://github.com/user-attachments/assets/ed8be4a7-fbe3-4e7a-af35-fdb82a38f267" />

상태 코드 분석 진행~~~
<img width="1280" height="823" alt="week02-02" src="https://github.com/user-attachments/assets/94cbbf04-9e4c-475d-bc15-5c96ee974c3e" />

cf) 응답 패킷 해석 - 상태 코드 
<img width="1206" height="538" alt="week02-03" src="https://github.com/user-attachments/assets/bf38667f-309e-49cd-87d5-aeb7c2890d3d" />

2xx: 214개
3xx: 8개
4xx,5xx:오류 없음
리다이렉션은 HTTP 전환 과정에서 발생한 것으로 보인다.



