# 풀이과정

1. Proxy 설정에서 'Response interception rules' 아래 빈칸을 선택해 응답을 가로챌 수 있도록 설정한다.

2. Proxy 옵션을 선택하여 해당 화면에 있는 'Open browser'를 통해 브라우저를 열고 학교 홈페이지에 접속한다.

3. 'Intercept on'으로 변경하고 홈페이지를 새로 고침하고 'Forward'를 한다.

4. 응답 패킷의 HTML 코드에서 "덕성안내"부분을 찾아 변조한다.

5. 변조 후에 'Forward' 하고 'Intercept off' 하면 직접 작성한 내용으로 변경된다.

# 결과 화면 

<img width="2074" height="944" alt="Image" src="https://github.com/user-attachments/assets/b6c91008-cce3-4cb8-bd62-50d3434ce0e0" />