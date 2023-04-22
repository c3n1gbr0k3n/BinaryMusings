#include<stdio.h>

void run() {
	char buf[0x10];
	printf("hello\n");
	gets(buf);
}


int main() {
	run();
	return 0;
}
