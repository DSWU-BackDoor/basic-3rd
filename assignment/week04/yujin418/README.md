# 1. 진행 과정
1. Burp Suite 접속
2. Proxy 설정에서 응답도 가로챌 수 있도록 설정한다.   
3. [Open Browser]로 브라우저를 열고, 검색창에 duksung.ac.kr 검색  
5. [Intercept on]을 클릭하고, 홈페이지를 새로 고침하면 요청 패킷을 잡을 수 있다. 
6. Forward 하면, 응답 패킷이 잡힌 것을 확인할 수 있다. 
7. 응답 패킷의 HTML 코드에서 학교 홈페이지 왼쪽 상단 "창학 제106주년 기념식 안내” 부분을 찾아 변조한다. 
8. 변조 후 Forward → [Intercept off] 하고 결과 확인 

# 2. 캡쳐 사진
<img width="1888" height="999" alt="Image" src="https://github.com/user-attachments/assets/5a4b7dba-3fcd-4078-be63-7b013963fcbb" />