#include<stdio.h>

int main() {
    int num;
    printf("%300d%hhn\n", 0x12345678, &num);
    printf("%d\n", num);
}