#include<stdio.h>
char *bin_sh = "/bin/sh";
void hint();
asm(
    ".text\n"
    ".global hint\n"
    "hint:\n"
    "inc eax\n"
    "ret\n"
    "xor eax, eax\n"
    "xor ebx, ebx\n"
    "xor ecx, ecx\n"
    "xor edx, edx\n"
    "ret\n"
    "int 0x80\n"
);
void run() {
    char buf[0x10];
    printf("input: ");
    scanf("%s", buf);
};
int main() {
    run();
    return 0;
}
// gcc ret2syscall.c -o ret2syscall -no-pie -fno-pic -fno-stack-protector -m32 -masm=intel
