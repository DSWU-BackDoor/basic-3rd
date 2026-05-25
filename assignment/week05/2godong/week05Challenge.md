# 1. 드림핵 워게임 풀이

## 1-1. 워게임 [XSS 취약점]

XSS 취약점이란 웹 어플리케이션에서 사용자 입력 값에 대한 필터링이 제대로 이루어지지 않을 경우, 공격자가 입력이 가능한 폼에 스크립트 삽입이 가능하여 악의적인 스크립트가 희생자 측에서 동작하도록 하는 취약점을 말함.
공격자는 취약점을 이용하여 사용자의 개인정보 및 쿠키정보 탈취, 악성코드 감염, 웹 페이지 변조 등의 공격을 수행.

## 1-2. 사진

<img width="1618" height="352" alt="Image" src="https://private-user-images.githubusercontent.com/203046560/597476842-9434faac-8a43-4f0a-806f-369605dc6e7b.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzk2OTM0ODQsIm5iZiI6MTc3OTY5MzE4NCwicGF0aCI6Ii8yMDMwNDY1NjAvNTk3NDc2ODQyLTk0MzRmYWFjLThhNDMtNGYwYS04MDZmLTM2OTYwNWRjNmU3Yi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNTI1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDUyNVQwNzEzMDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jOGIzZGZhNGRkYmU3NDRmNjA5ZDkzZjE0MWU1YWVkZTA1ZWI4YjEyMDIzMmM2NjUzOGE4MzM2MDNmNDFhNWU4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.xvKxo1FYTejnHOJ-55O7BydccfbymZW1y-YGGKNqKWs" />

## 1-3. 풀이

- https://dreamhack.io/wargame/challenges/28 에서 문제 다운로드
- vscode에서 소스 코드 분석
- @app.route("/vuln") 부분에서 입력 값이 필터링 없이 그대로 반환. vuln 페이지에 들어갔을 때 url에 <script>가 그대로 뜨는 것을 보아, <script> 를 이용하는 것을 풀이 방법으로 추정.
- flag 페이지에 "test"를 입력하고 제출을 해보면 good가 출력됨.
- 다음으로 <script>location.href='/memo?memo='+document.cookie</script> 를 입력하고 제출하여 flag 값을 얻어낸다.
- 얻어낸 flag는 flag=DH{2c01577e9542ec24d68ba0ffb846508e}
- 값을 Submit Flag에 제출

# 2. VirtualBox & Ubuntu 설치 후 스크린샷

<img width="450" alt="스크린샷 2026-05-21 165844" src="https://github.com/user-attachments/assets/386142f8-5c00-4273-9157-b051ba958706" />
