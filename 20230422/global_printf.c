#include<stdio.h>
#include<stdlib.h>
char buf[0x50];
void hint() { system("/bin/sh"); }
int main() {
    int choice;
    setbuf(stdout, 0);
    while(1) {
        scanf("%d", &choice);
        if(choice == 1) {
            scanf("%s", buf);
            printf(buf);
        } else {
            exit(0);
            // break;
        }
    }
}
// gcc global_printf.c -o global_printf -m32 -no-pie

