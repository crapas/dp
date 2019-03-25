#include <stdio.h>

int combination(int n, int m)
{
  if(n == 0 || m == 0 || n == m)
    return 1;
  else
    return combination(n - 1, m) + combination(n - 1, m - 1);
}

int main()
{
  printf("두 수 n, m을 입력하세요. (n >= m) : ");
  int n, m;
  scanf("%d %d", &n, &m);
  printf("C(%d, %d) = %d\n", n, m, combination(n, m));
  return 0;
}