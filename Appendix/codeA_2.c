#include <stdlib.h>
#include <stdio.h>
#include <time.h>

void linear(int N)
{
  int number[N];
  srand(time(NULL));
  for(int i = 0; i < N; i++)
  {
    number[i] = rand();
  }

    for(int i = 0; i < N; i++)
  {
    printf("%d\n", number[i]);
  }

}

int main()
{
  linear(10);
}