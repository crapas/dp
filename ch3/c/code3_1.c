#include <stdio.h>

int fibonacci(int n)
{
  // 피보나치 수를 저장하는 배열
  int arr[n + 1];
  arr[1] = 1;
  arr[2] = 1;
  for(int i = 3; i <= n; i++)
  {
    // 피보나치 수열의 n번째 항을 계산하고 이를 저장
    arr[i] = arr[i - 1] + arr[i - 2];
  }

  return arr[n];
}

int main()
{
  printf("숫자를 입력하세요 : ");
  int n;
  scanf("%d", &n);
  printf("피보나치 수열의 %d번째 항은 %d입니다.\n", n, fibonacci(n));
}