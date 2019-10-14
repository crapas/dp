#include <stdio.h>
#include <limits.h>

// n층의 빌딩, x개의 달걀
int eggDropTrial(int n, int x)
{
  // 0층은 0번, 1층은 1번 던져보면 되며, 
  // 만약 달걀이 1개인 경우 1층부터 꼭대기까지 n번 던져봐야 합니다.
  if(n == 1 || n == 0 || x == 1)
    return n;
  
  int minTrial = INT_MAX;

  for(int p = 1; p <= n; p++)
  {
    int broken = eggDropTrial(p - 1, x - 1);  // 깨진 경우 - 아래층으로
    int notBroken = eggDropTrial(n - p, x);   // 깨지지 않은 경우 - 위층으로
    // 최악의 경우이므로 두 경우 중 큰 값이 필요합니다.
    int thisTrial = broken > notBroken? broken: notBroken;
    // 최악의 경우의 최솟값 이므로 최솟값을 구합니다.
    minTrial = minTrial > thisTrial? thisTrial: minTrial;
  }  
  // 1번 던진 후의 결과이므로 1을 더해서 반환합니다.
  return minTrial + 1;
}

int main()
{
  // 빌딩 층수
  int n;
  // 달걀의 수
  int x;
  printf("빌딩의 층수와 달걀의 개수를 입력하세요 :");
  scanf("%d %d", &n, &x);
  printf("%d층의 빌딩과 %d개의 달걀이 있을 때 최악의 경우 최소 %d회 떨어뜨려야 합니다.\n",
          n, x, eggDropTrial(n, x));
  return 0;
}