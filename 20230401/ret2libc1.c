#include<stdio.h>
#include<stdlib.h>
char *p = "/bin/sh";
void hint() {
    system("echo hello");
}

void run() {
    char buf[0x10];
    gets(buf);
}

int main() {
    run();
    return 0;
}
