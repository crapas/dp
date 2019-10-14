#include <stdio.h>

void swap(int *a, int *b)
{
  *a ^= *b;
  *b ^= *a;
  *a ^= *b;
}

void bubbleSort(int *arr, int n)
{
  // 종료 조건
  if(n == 1)
    return;
  // 1회의 탐색 과정을 수행
  for(int j = 0; j < n - 1; j++)
    if(arr[j] > arr[j + 1])
      swap(&arr[j], &arr[j + 1]);
  // 더 작은 범위의 인수로 재귀 호출
  bubbleSort(arr, n - 1);
}

int main()
{
  int a[] = {10, 2, 6, 4, 5, 3, 2, 8};
  int size = sizeof(a) / sizeof(int);

  printf("원래 순서 : ");
  for(int i = 0; i < size; i++)
    printf("%d ", a[i]);
  
  bubbleSort(a, size);
  
  printf("\n정렬 결과 : ");
  for(int i = 0; i < size; i++)
    printf("%d ", a[i]);
  printf("\n");
}