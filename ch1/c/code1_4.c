#include <stdio.h>

int sum(int n)
{
	int sum = 0;
	for(int i = 1; i <= n; i++)
		sum += i;
	return sum;
}

int main()
{  
  printf("숫자를 하나 입력하세요 :");
  int x;
  scanf("%d", &x);
  printf("1에서 %d까지의 합 : %d\n", x, sum(x));
  return 0;
}