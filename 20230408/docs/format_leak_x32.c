#include<stdio.h>
#include<stdlib.h>

int main() {
    setbuf(stdout, 0);
    char buf[0x10];
    printf("input: \n");
    scanf("%16s", buf);
    printf(buf);
    return 0;
}