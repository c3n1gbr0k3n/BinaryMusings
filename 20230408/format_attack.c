#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<time.h>
int x;
int main() {
    setbuf(stdout, 0);
    char buf[0x10];
    memset(buf, 0, 0x10);
    int guess;
    srand(time(0));
    x = rand();
    printf("name: ");
    read(0, buf, 0x10);
    printf(buf);
    scanf("%d", &guess);
    if(guess == x) {
        system("/bin/sh");
    } else {
        printf("错误\n");q
    }
    return 0;
}