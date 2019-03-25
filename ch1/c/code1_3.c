#include <stdio.h>

int sum(int n)
{
	return (n <= 0)? 0: ((n == 1)? 1: (n + sum(n - 1)));
}

int main()
{  
  printf("숫자를 하나 입력하세요 :");
  int x;
  scanf("%d", &x);
  printf("1에서 %d 까지의 합 : %d\n", x, sum(x));
  return 0;
}