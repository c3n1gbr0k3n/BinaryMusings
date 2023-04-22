from pwn import*
o = process("./format_attack")
elf = ELF("./format_attack")
print(hex(elf.sym['x']))