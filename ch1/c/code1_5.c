#include <stdio.h>

int power(int x, int n)
{
	if(n == 0)
		return 1;
	else if(x == 1)
		return x;
	else
		return x * power(x, n - 1);
}

int main()
{
  printf("두 수를 입력하세요 : ");
  int x, n;
  scanf("%d %d", &x, &n);
  printf("%d^%d = %d\n", x, n, power(x, n));
}