#include<stdio.h>
int num = 7;
int main() {
    setbuf(stdout, 0);
    char buf[0x10];
    scanf("%s", buf);
    printf(buf);
    if(num == 10) {
        system("/bin/sh");
    } else {
        printf("err\n");
    }
}