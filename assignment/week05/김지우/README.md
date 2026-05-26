
1. Virtual Box 및 Ubuntu 설치
<img width="2464" height="1572" alt="Image" src="https://github.com/user-attachments/assets/8f61a6ff-5815-4017-be1c-6324e5feb4b0" />
이번 실습에서는 VirtualBox 환경에서 Ubuntu를 설치하는 과정에서 발생한 오류를 해결하는 경험을 다루었다. 초기에는 최신 버전인 Ubuntu 26.04를 사용하여 가상머신에 설치를 진행하였으나, 부팅 과정에서 vmwgfx seems to be running on an unsupported hypervisor라는 에러 메시지가 발생하며 정상적으로 운영체제가 실행되지 않았다. 이후 화면이 멈추거나 검은 화면만 출력되는 문제가 지속적으로 발생하여 설치가 불가능한 상태였다.

해당 문제의 원인을 분석한 결과, vmwgfx는 VMware 환경에서 사용하는 그래픽 드라이버인데, 이를 VirtualBox 환경에서 실행하려 하면서 호환성 문제가 발생한 것으로 판단하였다. 특히 Ubuntu 26.04와 같은 최신 버전은 가상화 환경과의 드라이버 호환성이 완전히 검증되지 않은 경우가 있어 이러한 충돌이 발생할 수 있다.

문제를 해결하기 위해 여러 가지 방법을 시도하였다. 먼저 VirtualBox의 디스플레이 설정에서 Graphics Controller를 VMSVGA로 변경하고 3D Acceleration을 비활성화하는 등 그래픽 설정을 조정하였다. 이후 Safe Graphics 모드를 통해 최소한의 그래픽 드라이버로 부팅을 시도하였으나, 여전히 검은 화면에서 멈추는 현상이 발생하였다. 추가적으로 GRUB 설정에서 nomodeset 옵션을 적용하여 그래픽 드라이버 로딩을 제한하는 방법도 고려하였으나, 근본적인 해결에는 이르지 못하였다.

결과적으로 해당 문제는 단순한 설정 오류가 아니라 Ubuntu 26.04 버전과 VirtualBox 환경 간의 구조적인 호환성 문제로 판단하였다. 이에 따라 보다 안정적인 환경을 위해 Ubuntu 22.04 LTS 버전으로 변경하여 설치를 다시 진행하였다. 그 결과 별다른 오류 없이 정상적으로 부팅 및 설치가 완료되었으며, 이후 시스템도 안정적으로 동작하였다.



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