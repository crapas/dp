#include <stdio.h>

void towerOfHanoi(char s, char d, char e, int n)
{
	// 종료 조건
	if(n <= 0)
		return;
	towerOfHanoi(s, e, d, n - 1);
	printf("%d번 원반을 %c에서 %c로 옮깁니다.\n", n, s, d);
	towerOfHanoi(e, d, s, n - 1);
}

int main()
{
  printf("원반의 수를 입력하세요 : ");
  int n;
  scanf("%d", &n);
  
  towerOfHanoi('s', 'd', 'e', n);
}