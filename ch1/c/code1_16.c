#include <stdio.h>

// 로딩 타임에 데이터 영역에 할당되며 0으로 초기화
int total;

/** 함수의 코드는 코드 영역으로 들어갑니다. 실행타임에 이 함수가
 * 호출될 때 활성 레코드는 스택의 최상단에 생성되며 정적 변수가
 * 아닌 지역 변수(x와 y)의 메모리도 활성 레코드 안에 할당됩니다.
 * count는 정적 변수이므로 로드타임에 데이터 영역에 할당됩니다.
 */
int squareOfSum(int x, int y)
{
  static int count = 0;	// 로드타임 변수
  printf("함수가 %d번 호출되었습니다.\n", ++count);
  // square() 함수를 호출하지 않습니다.
  // 함수 호출 횟수를 줄여 코드를 개선할 수 있습니다.  
	return (x + y) * (x + y);
}

/** main 함수의 코드도 코드 영역으로 들어갑니다. main 함수가
 * 호출되면 스택의 최상단에 활성 레코드가 생성되며 정적 변수가 
 * 아닌 지역 변수(a와 b)는 이 활성 레코드 내에 할당됩니다.
 */
int main()
{
  int a = 4, b = 2;
  total = squareOfSum(a, b);
  printf("합의 제곱 = %d\n", total);
}
