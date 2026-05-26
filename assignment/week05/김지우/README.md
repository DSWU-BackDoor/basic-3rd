1. Virtual Box 및 Ubuntu 설치
<img width="2464" height="1572" alt="Image" src="https://github.com/user-attachments/assets/8f61a6ff-5815-4017-be1c-6324e5feb4b0" />

2. 워게임
<img width="2879" height="1799" alt="Image" src="https://github.com/user-attachments/assets/90f868ca-b2bb-4b41-930d-f5ac070fba60" />
<img width="2879" height="1695" alt="Image" src="https://github.com/user-attachments/assets/e2208543-2d34-4b62-a38e-f992cfecd0ca" />

이번 문제는 XSS를 이용해서 flag를 얻는 문제였다. 처음 코드를 확인했을 때 /vuln에서 입력값을 그대로 출력하는 부분이 보여서 XSS가 가능하겠다고 생각했다. <script>alert(1)</script>를 넣어보니 실제로 alert 창이 떠서 취약점이 있다는 걸 확인할 수 있었다.

이후 /flag를 보니 Selenium으로 동작하는 봇이 입력값을 확인하는 구조였고, 이 봇이 flag를 쿠키에 담아서 페이지에 접속한다는 것을 알게 됐다. 이 부분을 보고 XSS로 document.cookie를 가져오면 flag를 얻을 수 있겠다고 판단했다.

문제는 이 값을 어디로 보내야 하는지였다. 외부 서버를 사용하는 방법도 있지만, 코드에 /memo 기능이 있는 것을 보고 이걸 활용할 수 있겠다고 생각했다. 해당 페이지는 입력값을 저장해서 다시 보여주는 구조였고, 별다른 검증도 없었다.

먼저 <script>location.href="/memo?memo=test"</script>를 넣어서 값이 저장되는지 확인했다. /memo 페이지에 들어가보니 test가 정상적으로 저장된 것을 확인할 수 있었다. 이 과정을 통해 같은 방식으로 쿠키 값도 전달할 수 있겠다고 판단했다.

이후 <script>location.href="/memo?memo="+document.cookie</script> 형태로 payload를 만들었다. 해당 코드는 현재 페이지의 쿠키 값을 읽어서 /memo로 보내는 역할을 한다.

이 payload를 /flag에 입력하면 봇이 /vuln에 접속하면서 스크립트가 실행되고, 그 결과 flag가 /memo에 저장된다. 이후 /memo 페이지에 접속하니 flag=DH{...} 형태로 값이 저장된 것을 확인할 수 있었고, 이를 통해 flag를 얻을 수 있었다.

이번 문제를 풀면서 XSS가 단순히 alert를 띄우는 것에서 끝나는 것이 아니라 실제로 데이터를 가져오는 데 활용된다는 점을 이해하게 됐다. 처음에는 payload를 만드는 과정이 어렵게 느껴졌지만, 단계별로 테스트하면서 접근하는 방식이 도움이 됐다.