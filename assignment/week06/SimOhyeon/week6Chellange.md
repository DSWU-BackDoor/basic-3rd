### level 0
ssh를 이용해 원격으로 bandit.labs.overthewire.org를 접속하는 문제입니다.
접속하기 위해서는
```
ssh bandit0@bandit.labs.overthewire.org -p 2220
```
라는 명령어를 입력하면 됩니다.

![bandit wargame]({{ '/images/0.png' | relative_url }})

---

### level 0 -> 1
readme 파일을 열어 그 안에 있는 비밀번호를 읽는 문제입니다.
문제를 읽기 위해서는 파일 내용을 출력하는 cat이라는 명령어가 필요합니다.
```
cat readme
```
![bandit wargame]({{ '/images/1.png' | relative_url }})

---

### level 1 -> 2
이번 문제는 홈 디렉터리에 있는 '-' 라는 파일을 열어 비밀번호를 찾아야합니다.
그러나 특수문자인 '-'는 그저 cat이라는 명령어를 그냥 써서 열리지 않습니다.
그렇기에 현재 경로를 명시해줘야 합니다.
```
cat ./-
```
![bandit wargame]({{ '/images/2.png' | relative_url }})

---

### level 2 -> 3
이번 파일의 제목은 --spaces in this filename--이라는 좀 특이한 이름을 가지고 있습니다.
그렇기에 그냥 cat으로 못 열기 때문에 리다이렉션을 이용해 열어줍니다.
리다이렉션을 쓰면 대상 파일의 내용을 복사하거나 생성, 합치거나 파일의 내용을 명령에 입력할 수 있습니다.
방향에 따라 다른데, < 방향은 후자입니다.
```
cat < --spaces in this filename--
```
![bandit wargame]({{ '/images/3.png' | relative_url }})

---

### level 3 -> 4

이번 문제는 숨어있는 파일을 찾아내어 그 안에 있는 비밀번호를 뜯는 문제입니다.
ls를 이용하면 그 디렉터리 안에 있는 파일을 볼 수 있는데, 숨어있는 것도 보기 위해서는
-a라는 옵션을 이용해 숨겨져 있는 파일까지 모두 보여달라 해야합니다.
```
cd inhere
ls -a
cat ...Hiding-From-You
```
![bandit wargame]({{ '/images/4.png' | relative_url }})

---

### level 4 -> 5

inhere 디렉토리 어딘가에 있는 사람이 읽을 수 있고 크기는 1033바이트인 실행불가 파일을 열어야합니다.
그렇기에 파일 종류를 확인할 수 있는 file이라는 명령어로 찾아줄 것입니다.
file 뒤에 사용된 ./-*으로 -로 시작하는 모든 파일을 확인해줄 것입니다.
결과에 나온 파일 중 읽을 수 있는 ASCII text인 -file07을 확인해주겠습니다.
```
cd inhere
file ./-*
cat ./-file07
```
![bandit wargame]({{ '/images/5.png' | relative_url }})