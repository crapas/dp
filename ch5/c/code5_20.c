#include <stdio.h>
#include <string.h>

int LPS_length(char *str, int start, int end)
{
  // 종료 조건 : start >= end
  if(start > end)
    return 0;
  if(start == end)
    return 1;
    
  // 첫 글자와 끝 글자가 같을 때
  if(str[start] == str[end])
    return LPS_length(str, start + 1, end - 1) + 2;
  else{
    int left = LPS_length(str, start, end - 1);
    int right = LPS_length(str, start + 1, end);
    // 앞의 예제에서는 getMax라는 별도의 함수를 사용했습니다.
    // 아래와 같이 함수 호출 없이 구현해서 성능을 높일 수 있습니다.
    return left > right? left: right;
  }          
}

int main()
{
  char str[] = "BBABCBCAB";
  int start = 0;
  int end = strlen(str) - 1;
  printf("%s의 최대 회문 부분 수열의 길이는 %d입니다.\n", 
         str, LPS_length(str, start, end));
  return 0;
}