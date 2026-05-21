# 1. 캡쳐 사진

<img width="1622" height="1697" alt="Image" src="https://github.com/user-attachments/assets/965acde7-83d1-435e-8245-c0d9666a4bd1" />

# 2. 진행 과정

1. Burp Suite 접속
2. Proxy 설정에서 응답을 가로챌 수 있도록 설정.
3. Open Browser를 통해 브라우저를 열어 학교 홈페이지에 접속.
4. Intercept on을 클릭하고 학교 홈페이지 새로고침.
   4-1. 요청 패킷이 잡혔는지 확인.
5. Request를 Forward.
   5-1. 응답 패킷이 잡혔는지 확인.
6. Response -> pertty의 HTML부분에서 변조하고자 하는 메시지 수정.
7. 변조 후 Foward, Intercept off.
8. 홈페이지를 새로고침하여 변조된 내용 확인
