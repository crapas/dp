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
  // 종료 조건 : 남은 물건이 없거나 배낭이 가득 찼을 때
  if(n <= 0 || C <= 0)
    return 0;

  // n번째 물건의 무게가 C보다 크면 그 물건은 넣을 수 없습니다.
  // 하지만 남은 물건 중에 C보다 작은 다른 물건이 있을지도 모릅니다.
  if(weight[n - 1] > C)
    return knapSack(C, weight, value, n - 1);

  // n번째 물건을 배낭에 넣는 경우
  int carry = value[n - 1] + 
              knapSack(C - weight[n - 1], weight, value, n - 1);
  // n번째 물건을 놔두는 경우
  int leave = knapSack(C, weight, value, n - 1);

  return getMax(carry, leave);
}

int main()
{
  int weight[] = {2, 3, 4, 5};
  int value[] = {3, 4, 5, 6};
  printf("도둑이 가지고 갈 수 있는 가치의 최댓값은 %d입니다.\n", 
         knapSack(5, weight, value, 4));
  return 0;
}