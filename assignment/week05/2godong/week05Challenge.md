# 1. 드림핵 워게임 풀이

## 1-1. 워게임 [XSS 취약점]

XSS 취약점이란 웹 어플리케이션에서 사용자 입력 값에 대한 필터링이 제대로 이루어지지 않을 경우, 공격자가 입력이 가능한 폼에 스크립트 삽입이 가능하여 악의적인 스크립트가 희생자 측에서 동작하도록 하는 취약점을 말함.
공격자는 취약점을 이용하여 사용자의 개인정보 및 쿠키정보 탈취, 악성코드 감염, 웹 페이지 변조 등의 공격을 수행.

## 1-2. 사진

<img width="1645" height="464" alt="Image" src="https://github.com/user-attachments/assets/b1717f20-d2f2-4807-92b2-bf21e4948cb6" />

## 1-3. 풀이

- https://dreamhack.io/wargame/challenges/28 에서 문제 다운로드
- vscode에서 소스 코드 분석
- @app.route("/vuln") 부분에서 입력 값이 필터링 없이 그대로 반환. vuln 페이지에 들어갔을 때 url에 <script>가 그대로 뜨는 것을 보아, <script> 를 이용하는 것을 풀이 방법으로 추정.
- flag 페이지에 "test"를 입력하고 제출을 해보면 good가 출력됨.
- 다음으로 <script>location.href='/memo?memo='+document.cookie</script> 를 입력하고 제출하여 flag 값을 얻어낸다.
- 얻어낸 flag는 flag=DH{2c01577e9542ec24d68ba0ffb846508e}
- 값을 Submit Flag에 제출

# 2. VirtualBox & Ubuntu 설치 후 스크린샷

<img width="2055" height="1530" alt="Image" src="https://github.com/user-attachments/assets/c38e1594-3af3-4ab4-a4ad-40e3a21c24dd" />
