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