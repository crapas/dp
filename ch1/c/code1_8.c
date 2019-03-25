#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct node{
	struct node *left;		// 왼쪽 자식 노드의 트리를 가리키는 포인터
	char data;
	struct node *right;	// 오른쪽 자식 노드의 트리를 가리키는 포인터
} Node;

/* 트리의 중위 순회 탐색 결과를 출력합니다. */
void inOrder(Node* ptr)
{
	if(ptr == NULL)
		return;

	inOrder(ptr->left);
	printf("%c ", ptr->data);
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
Node* insertNode(Node* parent, char value, bool isleft)
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
  // tree의 root 생성. root는 isleft 값이 의미가 없습니다.
  Node* root = insertNode(NULL, 'A', true);
  insertNode(root, 'B', true);
  insertNode(root, 'C', false);
  insertNode(root->left, 'E', true);
  insertNode(root->right, 'F', true);
  insertNode(root->right, 'G', false);

  printf("중위 순회 탐색 결과 : ");
  inOrder(root);
  printf("\n");
  
  deleteTree(root);
  return 0;
}