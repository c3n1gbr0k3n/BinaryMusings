#include<stdio.h>
#include<stdlib.h>
int a = 0x12345678;
int main() {
    char buf[0x10];
    scanf("%16s", buf);
    printf(buf);
    printf("\na: %x\n", a);
    if(a == 0x12345604) {
        system("/bin/sh");
    } else {
        printf("err\n");
    }
    return 0;
}
