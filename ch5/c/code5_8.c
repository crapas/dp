#include <stdio.h>
#include <stdbool.h>

// n은 집합의 원소의 수입니다.
bool isSubsetSum(int* arr, int n, int X)
{
  int subsum[n][X + 1];

  for(int i = 0; i < n; i++)
  {
    for(int j = 0; j <= X; j++)
    {
      subsum[i][j] = false;
    }
  }

  // 첫 번째 열은 항상 참
  for(int i = 0; i < n; i++)
    subsum[i][0] = true;

  // 첫 번째 행은 j가 0 또는 arr[0]인 경우만 참
  for(int j = 1; j <= X; j++)
    if(arr[0] == j)
      subsum[0][j] = true;
    else 
      subsum[0][j] = false;
  
  // 나머지 셀을 채웁니다.
  for(int i = 1; i < n; i++)
{
    int v = arr[i];
    for(int j = 1; j <= X; j++)
{
      if(j < v)
        subsum[i][j] = subsum[i - 1][j];
      else if(subsum[i - 1][j])
        subsum[i][j] = true;
      else
        subsum[i][j] = subsum[i - 1][j - v];
    }
  }

  // 완성된 행렬을 출력해봅니다.
  for(int i = 0; i < n; i++)
  {
    for(int j = 0; j <= X; j++)
    {
      printf("%c ", subsum[i][j]? 'T': 'F');
    }
    printf("\n");
  }

  return subsum[n - 1][X];
}

int main()
{
  int arr[7] = {0, 6, 11, 8, 17, 3, 9};
  printf("결과는 %s입니다.\n", isSubsetSum(arr, 7, 13)? "참": "거짓");
  printf("결과는 %s입니다.\n", isSubsetSum(arr, 7, 14)? "참": "거짓");
  return 0;
}