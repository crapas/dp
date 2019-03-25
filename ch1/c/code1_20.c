#include <stdio.h>

int factorial(int n)
{
  int f = 1;
  for(int i = 2; i <= n; i++)
    f = f * i;
  return f;
}

int main()
{
  printf("숫자를 입력하세요 : ");
  int n;
  // 별로 크지 않은 숫자라도 계승의 값은 int 자료형의 
  // 범위를 넘어 갑니다. 수치 해석을 다루는 책이 아니므로
  // 이런 소소한 부분은 신경쓰지 않겠습니다.
  scanf("%d", &n);
  printf("%d! = %d입니다.\n", n, factorial(n));
}
