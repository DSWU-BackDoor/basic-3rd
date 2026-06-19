## 6주차 과제(Bandit)

## 사전 지식 정리
1) Bandit : Linux 명령어, 터미널 환경에 익숙해지기 위한 입문용 게임 
* 실습하며 명령어 익히는 것 중요 
2) SSH : 원격 컴퓨터에 안전하게 접속하기 위한 프로토콜 
* OverTheWire 서버(Bandit)의 리눅스 환경에서 실습 
3) 포트 번호-2220 : Bandit 전용 입구
* 일반적으로 SSH는 22번 포트

## 풀이 
1-1. ０단계 접속 시도－＞ 홈페이지에서 제공한 패스워드 이용해 접속 완료
<img width="786" height="366" alt="Image" src="https://github.com/user-attachments/assets/1901a6d1-5dac-4c3b-9239-83cb23930b2d" />

1-2. １단계의 비밀번호는 '홈디렉터리에 있는 readme파일'에 저장 되어있음 -> １）홈디렉터리로 이동： cd ~ ２）폴더 내의 파일 확인：ls -a ３）readme 파일 내의 작성된 패스워드 확인： cat readme
<img width="818" height="326" alt="Image" src="https://github.com/user-attachments/assets/5d15e88a-5b7d-4c31-9c57-71392f2b47b3" />

* 모든 단계는 ０단계와 동일하게 접속함.

2. ２단계의 비밀번호는 '홈 디렉터리에 위치한 - 파일'에 저장 되어있음 －＞ １）홈디렉터리로 이동 ２） -파일 내의 내용 확인： cat ./（특수문자이기에 작성 방식 다름）
<img width="524" height="60" alt="Image" src="https://github.com/user-attachments/assets/53c16252-7677-4674-b4a1-582f758bf954" />

3. ３단계의 비밀번호는 ‘홈 디렉터리에 위치한 --spaces in this filename-- 파일’에 저장 되어있음 －＞ １）홈디렉터리로 이동 ２）파일 내의 내용 확인： ｃａｔ －－ “ --spaces in this filename--”（특수한 이름이기에 작성 방식 다름）
<img width="748" height="142" alt="Image" src="https://github.com/user-attachments/assets/c09b9d4a-6e53-4784-bdbc-34d4dab55b84" />

4.４단계의 비밀번호는 ‘inhere 디렉터리에 위치한 숨겨진 파일’에 저장 되어있음 －＞ １）inhere 디렉터리로 이동： ｃｄ ｉｎｈｅｒｅ ２）파일 내의 내용 확인： ｃａｔ －－ “ 。。ＨＩｄｉｎｇ－Ｆｒｏｍ－Ｙｏｕ”（특수한 이름이기에 작성 방식 다름）
<img width="576" height="170" alt="Image" src="https://github.com/user-attachments/assets/ca5fb9ba-1398-41da-a42a-d57a2c278394" />

5. ５단계의 비밀번호는 ‘inhere 디렉터리에 위치한 파일 중 사람이 읽을 수 있는 파일’에 저장 되어있음 －＞ １）inhere 디렉터리로 이동： ｃｄ ｉｎｈｅｒｅ ２）디렉터리 내 파일의 종류 확인： ｆｉｌｅ 。／＊３）－ｆｉｌｅ０７파일 내의 내용 확인： ｃａｔ －－ “ －ｆｉｌｅ０７”（특수한 이름이기에 작성 방식 다름）
<img width="516" height="374" alt="Image" src="https://github.com/user-attachments/assets/c88ffe43-4128-418c-9091-b96fc4ef8933" />

6. ６단계의 비밀번호는 ‘inhere 디렉터리에 위치한 사람이 읽을 수 있는 １０３３바이트 크기의 파일’에 저장 되어있음 －＞ １）inhere 디렉터리로 이동： ｃｄ ｉｎｈｅｒｅ ２）디렉터리 내 파일 중 해당 조건 만족하는 파일 찾기： find . -type f -size 1033c ! -executable ３）파일 내의 내용 확인： cat ./maybehere07/.file2
<img width="710" height="134" alt="Image" src="https://github.com/user-attachments/assets/c5453691-943f-41f4-a350-adbf8e1c8f17" />