#include <stdio.h>

void fun()
{
  int a = 5;
  // 다음 행에서 컴파일 오류가 발생합니다.
  static int b = a;
  printf("Value: %d\n", b);
}

int main()
{
  fun();
}