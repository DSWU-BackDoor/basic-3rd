# week06 과제

## Level 0→1
Q. The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH.


ls로 현재 디렉터리 파일 확인하면 readme 파일이 보인다. cat readme로 파일 내용을 읽는다. 
![실행 결과](01.png)


## Level 1→2
Q. The password for the next level is stored in a file called - located in the home directory


홈 디렉터리에 - 라는 이름의 파일이 있는데, cat - 라고 쓰면 - 를 표준 입력의 의미로 해석하기 때문에 - 가 파일 이름이라는 것을 명시해야 한다. ./- 는 현재 디렉터리에 있는 이름이 - 인 파일이라는 의미이므로 cat ./- 와 같이 명령어를 입력한다. 
![실행 결과](02.png)


## Level 2→3
Q. The password for the next level is stored in a file called --spaces in this filename-- located in the home directory


리눅스에서는 공백이 명령어 구분으로 사용되기 때문에 파일 이름에 공백이 포함된다면 파일 이름 전체를 하나로 묶어줘야 한다. cat "./--spaces in this filename--" 와 같이 파일의 이름을 큰 따옴표나 작은 따옴표로 감싸서 명령어를 입력한다. 
![실행 결과](03.png)


## Level 3→4
Q. The password for the next level is stored in a hidden file in the inhere directory.


inhere 디렉터리의 숨김 파일을 찾아야 하기 때문에 cd inhere을 통해 inhere 디렉터리로 이동한다. 숨김 파일까지 포함해서 보기 위하여 ls -a을 입력하면, 숨김 파일의 이름을 알 수 있다. cat ...Hiding-From-You(찾은 숨김 파일의 이름)을 입력한다. 
![실행 결과](04.png)


## Level 4→5
Q. The password for the next level is stored in the only human-readable file in the inhere directory. 


inhere 디렉터리 안에 있는 여러 파일 중 사람이 읽을 수 있는 내용의 파일을 찾아야 한다. cd inhere을 통해 inhere 디렉터리로 이동한다. file ./* 을 통해 파일 종류를 확인한다. 그 중 ./-file07: ASCII text가 사람이 읽을 수 있는 내용의 파일이므로, cat ./-file07을 입력한다.
![실행 결과](05.png) 
