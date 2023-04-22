#include<stdio.h>
int main() {
    int a = 10;
    printf("%d\n", a);
    printf("%x\n", a);
    printf("%p\n", &a);    // 打印的是a的地址
    printf("aaaa%n\n", &a);    // 写入变量a中
    printf("%d\n", a);
    return 0;
}