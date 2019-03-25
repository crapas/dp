#include <stdio.h>
#include <limits.h>

int maxSubArraySum(int* arr, int n)
{
  int maxSum = INT_MIN;
  int tempSum = 0;

  for(int i = 0; i < n; i++)
  {
    tempSum = 0;
    for(int j = i; j < n; j++)
    {
      // tempSum은 현재의 인덱스 i에서 인덱스 j까지의 배열의
      // 숫자의 합을 저장합니다.
      tempSum += arr[j];
      if(tempSum > maxSum)
        maxSum = tempSum;
    }
  }
  return maxSum;
}

int main()
{
  int arr[] = {-2, -3, 4, -1, -2, 1, 5, -3};
  int n = sizeof(arr) / sizeof(int);
  printf("부분 배열의 합의 최대값은 %d입니다.\n", maxSubArraySum(arr, n));
  return 0;
}