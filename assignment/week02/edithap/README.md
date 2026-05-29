1. 분석 목표
Wireshark를 이용하여 PDF 파일 다운로드 패킷을 캡처한다.
HTTP 상태 코드를 분석한다.

2. 분석 과정
① Wireshark 실행 및 캡처 시작
 Wireshark를 실행한 후, 노트북에서 사용 중이었던 Wi-Fi를 선택하여 패킷 캡처를 시작하였다.

② 디스플레이 필터 설정
 HTTP 패킷만 확인하기 위해 디스플레이 필터에 http를 적용하였다.

③ 사이트 접속 및 암호화 해제
 HTTPS 통신은 암호화되어 패킷 내용을 확인할 수 없기 때문에, HTTPS를 HTTP로 변경하여 평문 패킷이 보이도록 설정하였다.

④ PDF 파일 다운로드
 웹사이트에 접속하여 PDF 파일을 다운로드하였다.
 다운로드 과정에서 보안 경고창이 발생하였으나, 계속 진행을 선택하여 다운로드를 완료하였다.
 이후 Wireshark에서 PDF 파일 다운로드 관련 HTTP 패킷이 정상적으로 캡처된 것을 확인하였다.

⑤ 상태 코드 분석
 캡처된 HTTP 패킷을 분석한 결과는 다음과 같다.

 <img width="979" height="601" alt="스크린샷 2026-03-31 112638" src="https://github.com/user-attachments/assets/bc46cd67-5b57-4968-841b-e11e1fa19fce" />

 HTTP Response Packets: 1개
 2xx (Success): 1개 (200 OK)
 3xx (Redirection): 없음
 4xx (Client Error): 없음
 5xx (Server Error): 없음
 기타 오류 (broken): 없음

 따라서 모든 HTTP 응답은 정상 상태 코드(200 OK) 로 처리되었으며, 오류 및 리다이렉션 응답은 발생하지 않은 것으로 확인된다.
 또한 HTTP 통신은 포트 80번을 사용하는 것을 확인하였다.
