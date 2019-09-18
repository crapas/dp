#include <stdio.h>

int waysToScore(int n)
{
  // 변수를 사용해 선언한 배열은 초기화를 할 수 없습니다. 
  // 즉 int arr[n + 1] = {0}은 컴파일 에러가 발생합니다.
  int arr[n + 1];	
  for(int i = 0; i <= n; i++)
    arr[i] = 0;

  arr[0] = 1;		// 0점까지의 경우의 수는 아무것도 하지 않는 1가지입니다.

  for(int i = 1; i <= n; i++)
  {
    if(i - 3 >= 0)
      arr[i] += arr[i - 3];
    if(i - 5 >= 0)
      arr[i] += arr[i - 5];
    if(i - 10 >= 0)
      arr[i] += arr[i - 10];
  }
  return arr[n];
}

int main()
{
  printf("목적 점수를 입력하세요 : ");
  int N;
  scanf("%d", &N);
  printf("%d점까지의 경우의 수는 %d입니다.\n", N, waysToScore(N));
  return 0;
}