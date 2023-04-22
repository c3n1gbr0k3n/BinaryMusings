#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int num;
int main() {
    setbuf(stdout, 0);
    char buf[0x10];
    int guess;
    srand(time(0));
    num = rand();
    printf("input: ");
    scanf("%s", buf);
    printf(buf);
    scanf("%d", &guess);
    if(guess == num) {
        system("/bin/sh");
    } else {
        printf("err\n");
    }
}