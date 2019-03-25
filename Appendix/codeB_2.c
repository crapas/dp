#include <stdio.h>

void swap(int *a, int *b)
{
  *a ^= *b;
  *b ^= *a;
  *a ^= *b;
}

void bubbleSort(int *arr, int n)
{
  for(int i = 0; i < n - 1; i++)
    for(int j = 0; j < n - i - 1; j++)
      if(arr[j] > arr[j + 1])
        swap(&arr[j], &arr[j + 1]);
}

int solution(int A[], int N) {
  bubbleSort(A, N);
  for(int i = 0; i < N; i++)
  {
    if(i + 1 != A[i])
      return i + 1;
  }
  return N + 1;
}

int main()
{
  int A[1000];
  for(int i = 0; i < 1000; i++)
  {
    // 1001, 1000, ..., 503, 501, ..., 1의 테스트 케이스를 만듭니다.
    if(i <= 500)
      A[999 - i] = i + 1;
    else
      A[999 - i] = i + 2;   
  }

  printf("빠진 값은 %d입니다.\n", solution(A, 1000));
  return 0;
}