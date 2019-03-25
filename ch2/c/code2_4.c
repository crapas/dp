#include <stdio.h>

// 피보나치 수열의 47번째 항이 INT_MAX보다 클 수 있습니다.
// (시스템과 컴파일러의 종류에 따라 달라집니다.)
#define N 47

// 이 배열의 k번째 원소에 fibonnaci(k)의 결과를 저장합니다.
// fibonacci(k)가 계산 전이라면 memo[k]의 값은 0이 됩니다.
int memo[N] = {0};

int fibonacci(int n)
{
  // 만약 fibonacci(n)을 이미 계산했다면 다시 계산하지 않습니다.
  if(memo[n] != 0)
    return memo[n];

  // fibonacci(n)을 계산해 이 값을 memo[n]에 저장합니다.
  if(n == 1 || n == 2)
    memo[n] = 1;
  else
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2);

  return memo[n];
}


int main()
{
  printf("숫자를 입력하세요 : ");
  int n;
  scanf("%d", &n);
  printf("피보나치 수열의 %d번째 항은 %d입니다.\n", n, fibonacci(n));
}