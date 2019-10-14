#include <stdio.h>
#include <stdbool.h>

// n은 집합의 원소의 수입니다.
bool isSubsetSum(int* arr, int n, int X)
{
  // 종료 조건 1 : X가 0이면 성공 종료 조건입니다.
  if(X == 0)
    return true;

  // 종료 조건 2 : X가 0이 아니고 남은 원소가 없다면 실패 종료 조건입니다.
  if(n == 0)
    return false;

  // X보다 큰 원소는 무시해도 좋습니다.
  if(arr[0] > X)
    return isSubsetSum(arr + 1, n - 1, X);

  // 부분집합에 원소를 포함시키지 않는 경우와
  // 원소를 포함시키는 경우 각각에 대해 재귀 호출합니다.
  return isSubsetSum(arr + 1, n - 1, X) ||        // 포함시키지 않는 경우
         isSubsetSum(arr + 1, n - 1, X - arr[0]); // 포함시키는 경우  
}

int main()
{
  int arr[7] = {0, 6, 11, 8, 17, 3, 9};
  printf("결과는 %s입니다.\n", isSubsetSum(arr, 7, 13)? "참": "거짓");
  printf("결과는 %s입니다.\n", isSubsetSum(arr, 7, 14)? "참": "거짓");

  return 0;
}