#include <stdio.h>

int sum(unsigned int n)
{
  if(n == 1)
    return 1;
  else
    return n + sum(n - 1);
}

int main()
{
  printf("숫자를 하나 입력하세요 :");
  int x;
  scanf("%d", &x);
  printf("1에서 %d 까지의 합 : %d\n", x, sum(x));
  return 0;
}