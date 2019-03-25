#include <stdio.h>

void fun1();
void fun2();
void fun3();

void fun1(){
  printf("fun1 실행\n");
  fun2();
}

void fun2(){
  printf("fun2 실행\n");
}

void fun3(){
  printf("fun3 실행...입니다만, 실행되지 않을겁니다.\n");
}

int main()
{
  fun1();
}