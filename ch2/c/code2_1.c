#include <stdio.h>

int fibonacci(int n)
{
  if(n == 1 || n == 2)
    return 1;
  else
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main()
{
  printf("숫자를 입력하세요 : ");
  int n;
  scanf("%d", &n);
  printf("피보나치 수열의 %d번째 항은 %d입니다.\n", n, fibonacci(n));
}