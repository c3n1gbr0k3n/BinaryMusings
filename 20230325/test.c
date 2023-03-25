void main();
asm(
	".text\n"
	".global main\n"
	"main:\n"
// write(1, "hello", 5)
	"mov rax,  0x6f6c6c6568\n"
	"push rax\n"
	"mov rsi, rsp\n"
	"mov rdi, 1\n"
	"mov rdx, 5\n"
	"mov rax, 1\n"
	"syscall"
);
