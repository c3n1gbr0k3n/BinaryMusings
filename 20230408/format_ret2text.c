#include<stdio.h>
#include<stdlib.h>
void hint() { system("/bin/sh"); }

int main() {
    setbuf(stdout, 0);
    char buf[0x10];
    scanf("%s", buf);
    printf(buf);
    scanf("%s", buf);
    return 0;
}