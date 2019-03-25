#include <stdio.h>
#include <stdlib.h>

typedef struct node{
  int data;
  struct node* next;
}Node;

/* 선행 재귀의 경우
 * 먼저 리스트의 나머지를 탐색하고 난 후에
 * 현재 노드의 값을 출력합니다. */
void traverse1(Node* head)
{
	if(head != NULL)
  {
		traverse1(head->next);
		printf("%d ", head->data);
	}
}

/* 후행 재귀의 경우
 * 현재 노드의 값을 출력한 다음
 * 리스트의 나머지를 탐색합니다. */
void traverse2(Node* head)
{
	if(head != NULL)
  {
		printf("%d ", head->data);
		traverse2(head->next);
	}
}

int main()
{
  Node *head;
  Node* l1 = (Node*)malloc(sizeof(Node));
  Node* l2 = (Node*)malloc(sizeof(Node));
  Node* l3 = (Node*)malloc(sizeof(Node));
  Node* l4 = (Node*)malloc(sizeof(Node));
  l1->data = 1;
  l2->data = 2;
  l3->data = 3;
  l4->data = 4;
  l1->next = l2;
  l2->next = l3;
  l3->next = l4;
  l4->next = NULL;

  printf("traverse1 함수(선행 재귀)의 출력 : ");
  traverse1(l1);
  printf("\ntraverse2 함수(후행 재귀)의 출력 : ");
  traverse2(l1);
  printf("\n");

  free(l1); free(l2); free(l3); free(l4);
  return 0;
}