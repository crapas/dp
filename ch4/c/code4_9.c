#include <stdio.h>
#include <limits.h>
#include <stdbool.h>

int maxSubArraySum(int* arr, int n)
{
  int maxValue = INT_MIN;
  bool allNegative = true;

  // 배열의 값이 모두 음수인 경우, 배열의 값 중 
  // 가장 큰 값을 반환하면 됩니다.
  for(int i = 0; i < n; i++)
  {
    if(arr[i] >= 0)
    {
      allNegative = false;
      break;
    }
    else
    {
      if(arr[i] > maxValue)
        maxValue = arr[i];
    }    
  }
  if(allNegative)
    return maxValue;


  int maxSumSoFar = 0;
  int maxSumEndingHere = 0;

  for(int i = 0; i < n; i++)
  {
    maxSumEndingHere += arr[i];

    if(maxSumEndingHere < 0)
      maxSumEndingHere = 0;

    if(maxSumSoFar < maxSumEndingHere)
      maxSumSoFar = maxSumEndingHere;

    printf("i = %2d, arr[i] = %2d, maxSumEndingHere : %2d, maxSumSoFar : %2d\n",
           i, arr[i], maxSumEndingHere, maxSumSoFar);
  }
  return maxSumSoFar;
}

int main()
{
  int arr[] = {-2, -3, 4, -1, -2, 1, 5, -3};
  int n = sizeof(arr) / sizeof(int);
  printf("부분 배열의 합의 최대값은 %d입니다.\n", maxSubArraySum(arr, n));
  return 0;
}