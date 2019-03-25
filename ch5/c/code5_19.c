#include <stdio.h>

// 두 값 중 큰 값을 반환하는 인라인 도우미 함수
// 인라인 함수는 컴파일시에 함수를 호출 위치에 복사하여
// 실제 함수 호출이 일어나지 않습니다. 함수 호출이 없는 만큼
// 더 빠르지만, 프로그램의 크기가 좀 더 커집니다.
// 사실 최근의 컴파일러는 이런 류의 최적화는 알아서 처리합니다.
extern inline int getMax(int a, int b)
{
  return a > b? a: b;
}

int knapSack(int C, int* weight, int* value, int n)
{
  // 도둑의 최대 이익을 저장하는 배열
  // maxValue[i][j]는 물건이 i개, 배낭의 공간이 j일 때의 값입니다.
  int maxValue[n + 1][C + 1];

  // 배낭의 공간이 0일 때 도둑은 아무것도 넣을 수 없습니다.
  for(int i = 0; i <= n; i++)
    maxValue[i][0] = 0;
  
  // 물건이 하나도 없을 때 도둑은 훔칠게 없습니다.
  for(int j = 0; j <= C; j++)
    maxValue[0][j] = 0;

  // 배열을 채워 넣습니다.
  for(int i = 1; i <= n; i++)
  {
    for(int j = 1; j <= C; j++)
    {
      if(weight[i - 1] <= j){
        int x = j - weight[i - 1];
        maxValue[i][j] = getMax(value[i - 1] + maxValue[i - 1][x], 
                                maxValue[i - 1][j]);
      }
      // 물건이 배낭의 용량보다 크면 따질 필요 없이 왼쪽 셀을 복사합니다.
      else
        maxValue[i][j] = maxValue[i - 1][j];    
    }
  }

  // 도둑의 이익표를 출력해 봅시다.
  for(int i = 0; i <= n; i++){
    for(int j = 0; j <= C; j++){
      printf("%3d", maxValue[i][j]);
    }
    printf("\n");
  }
  return maxValue[n][C];
}

int main()
{
  int weight[] = {2, 3, 4, 5};
  int value[] = {3, 4, 5, 6};
  printf("도둑이 가지고 갈 수 있는 가치의 최대값은 %d입니다.\n", 
         knapSack(5, weight, value, 4));
  return 0;
}