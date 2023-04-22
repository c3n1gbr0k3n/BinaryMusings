#include<stdio.h>
#include<stdlib.h>
void hint() { system("/bin/sh"); }
int main() {
	setbuf(stdout, 0);
	char buf[50];
	scanf("%50s", buf);
	printf(buf);
	exit(0);
}
	
