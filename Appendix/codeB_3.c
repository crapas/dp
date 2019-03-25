#include <stdio.h>
#include <stdlib.h>

int static compare(const void* a, const void *b)
{
  if(*(int*)a > *(int*)b)
    return 1;
  else if(*(int*)a < *(int*)b)
    return -1;
  else
    return 0;
}

int solution(int A[], int N) {
  qsort(A, N, sizeof(int), compare);
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