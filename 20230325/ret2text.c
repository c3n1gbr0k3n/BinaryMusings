#include<stdio.h>
#include<stdlib.h>
void hint() {
	system("$0");
}

int main() {
	char buf[0x10];
	printf("input: ");
	scanf("%s", buf);
	return 0;
}
// gcc ret2text.c -o ret2text -no-pie -fno-stack-protector
