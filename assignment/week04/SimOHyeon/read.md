# 4주차 과제

## 버프 스위트를 활용하여 학교 홈페이지 아무 곳에나 자신의 이름 적기

1. Burp Suite에서 프록시 설정을 한다.

2. 설정에서 Response interception rules를 활성화해 응답을 캡처한다.

3. 덕성여대 홈페이지에 접속하여 Interception을 킨 상태로 새로고침한다.

4. forward해서 response를 확인해서 변조할 부분을 찾아 변조해준다.

5. 다시 forward를 하고 Interception을 끄면 아래와 같은 결과가 나온다.

결과:
<img width="2080" height="1653" alt="Image" src="https://github.com/user-attachments/assets/0f4b21c4-d4ec-41e9-abd6-c4f827fc6d4e" />