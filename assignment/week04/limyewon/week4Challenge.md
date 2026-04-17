# 1. 캡쳐 사진
<img width="500" alt="image" src="https://github.com/user-attachments/assets/904ccf97-f3de-44a5-8c20-395ddd269f7e" />



# 2. 진행 과정
- Burp Suite 접속 후, proxy 탭으로 이동
- Open Browser 클릭해서 브라우저 열고 학교 홈페이지 접속
- Intercept On 클릭하고 브라우저 새로고침 -> 응답 패킷 잡힘
- Request를 Forward -> Response 도착
- Response에서 Raw 선택 후, 원하는 부분 메시지 수정
- Forward 후 Intercept Off -> 브라우저에서 수정된 부분 확인
