#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool isInterleaving(char* A, char* B, char* C)
{
  // 하위 문제의 계산 반복을 확인하기 위해 검사하는
  // 문자열을 출력해봅니다.
  printf("인터리빙 확인 : [%s] + [%s] => [%s]\n", A, B, C);

  // 만약 모든 문자열이 빈 문자열인 경우
  if(!(*A) && !(*B) && !(*C))
    return true;

  // A와 B 문자열의 길이의 합이 C 문자열의 길이와 다를 때
  if(strlen(A) + strlen(B) != strlen(C))
    return false;

  bool caseA = false; 
  bool caseB = false;

  // A의 첫 글자와 C의 첫 글자가 같은 경우
  if(*A == *C)
    caseA = isInterleaving(A + 1, B, C + 1);
  
  // B의 첫 글자와 C의 첫 글자가 같은 경우
  if(*B == *C)
    caseB = isInterleaving(A, B + 1, C + 1);

  // 두 경우 중 하나라도 참이면 인터리빙
  return (caseA || caseB);
}

int main()
{
  char a[10] = "bcc";
  char b[10] = "bbca";
  char c[10] = "bbcbcac";

  int check = isInterleaving(a, b, c);
  printf("%s는 %s와 %s의 인터리빙", c, a, b);
  if(check == true)
    printf("입니다.\n");
  else
    printf("이 아닙니다.\n");
  
  return 0;
}