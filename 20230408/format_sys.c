#include<stdio.h>
void hint() {
    system("/bin/sh");
}
int main() {
    char buf[50];
    scanf("%50s", buf);
    printf(buf);
    exit(0);
}