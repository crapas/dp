#include <stdio.h>

int fibonacci(int n)
{
  int a = 1, b = 1, c, cnt;
  if(n == 1 || n == 2)
    return 1;
  for(cnt = 3; cnt <= n; cnt++)
  {
    c = a + b;
    a = b;
    b = c;
  }
  return c;
}

int main()
{
  printf("숫자를 입력하세요 : ");
  int n;
  scanf("%d", &n);
  printf("피보나치 수열의 %d번째 항은 %d입니다.\n", n, fibonacci(n));
}