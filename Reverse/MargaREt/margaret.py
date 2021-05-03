#!/usr/bin/env python3
import pwn

pwn.context.clear(log_level='WARN')

flag = "shaktictf{0"
first = True
while True:
    for guess in range(0x21, 0x7f):
        if not first:
            p.close()
        first = False
        p = pwn.process('./margaret')
        p.readuntil('CTF!\n')
        p.sendline(flag + chr(guess))
        try:
            p.readline()
        except:
            flag += chr(guess)
            print(flag)
            break
