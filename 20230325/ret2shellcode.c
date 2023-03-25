#include<stdio.h>
char buf[0x50];

void run() {
    char name[0x10];
    printf("name: ");
    scanf("%s", name);
    printf("content: ");
    scanf("%s", buf);
}

int main() {
    run();
    return 0;
}
// gcc ret2shellcode.c -o ret2shellcode -m32 -no-pie -fno-pic -fno-stack-protector -z execstack
