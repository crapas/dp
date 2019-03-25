#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct node{
	struct node *left;		// 왼쪽 자식 노드의 트리를 가리키는 포인터	
  int data;
	struct node *right;	// 오른쪽 자식 노드의 트리를 가리키는 포인터
} Node;

void addChildSum(Node* ptr)
{
  if(ptr == NULL)  // 종료 조건
    return;

  // 왼쪽 자식 트리에 대해서 계산합니다.
  addChildSum(ptr->left);

  // 오른쪽 자식 트리에 대해서 계산합니다.
  addChildSum(ptr->right);

  int finalSum = ptr->data;
  if(ptr->left != NULL)
    finalSum += ptr->left->data;

  if(ptr->right != NULL)
    finalSum += ptr->right->data;

  ptr->data = finalSum;
}

/* 트리의 중위 순회 탐색 결과를 출력합니다. */
void inOrder(Node* ptr)
{
	if(ptr == NULL)
		return;

	inOrder(ptr->left);
	printf("%d ", ptr->data);
	inOrder(ptr->right);
}

void deleteTree(Node* ptr)
{
  if(ptr == NULL)
    return;
  deleteTree(ptr->left);
  deleteTree(ptr->right);
  free(ptr);

}

// parent가 NULL이면 새로운 트리를 생성합니다.
// parent가 NULL이 아니면 왼쪽 (isleft == true) 또는 오른쪽
// 자식 노드를 value 값으로 생성합니다.
Node* insertNode(Node* parent, int value, bool isleft)
{
  Node* thisNode = (Node*)malloc(sizeof(Node));
  thisNode->data = value;
  thisNode->left = NULL;
  thisNode->right = NULL;
  if(parent != NULL)
  {
    if(isleft)
      parent->left = thisNode;
    else
      parent->right = thisNode;
  }
  return thisNode;
}
  
int main()
{
  Node* root = insertNode(NULL, 2, true);
  insertNode(root, 4, true);
  insertNode(root, 1, false);
  insertNode(root->left, 6, true);
  insertNode(root->left, 9, false);
  insertNode(root->right, 2, false);
  insertNode(root->left->right, 3, true);

  printf("만들어진 트리를 중위 순회 탐색으로 출력 : ");
  inOrder(root);
  printf("\n");

  addChildSum(root);

  printf("하위 노드의 합으로 갱신된 트리를 중위 순회 탐색으로 출력 : ");
  inOrder(root);
  printf("\n");

  // 메모리 해제
  deleteTree(root);
  return 0;
}