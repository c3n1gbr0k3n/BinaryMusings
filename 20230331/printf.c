#include<stdio.h>
int p = 0;
int main() {
	char buf[0x20];
	int * ptr = &p;
	scanf("%s", buf);
	printf(buf);
	return 0;
}
