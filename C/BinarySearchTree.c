#include<stdio.h>
#include<stdlib.h>
#define True 1
#define False 0

struct Node* newNode(int);
struct Node* insert(struct Node*, int);
int search(struct Node*, int);
struct Node* delete(struct Node*, int);
void inorder(struct Node*);
void preorder(struct Node*);
void postorder(struct Node*);
struct Node* minimum(struct Node*);

struct Node
{
	int data;
	struct Node* left;
	struct Node* right;
};

int main()
{
	struct Node* root = (struct Node*)malloc(sizeof(struct Node));
	root = NULL;
	int choice, condition = True, value;
	while(condition)
	{
		printf("Enter :-\n1. To insert a node to the tree.\n2. To search for an element in the tree.\n3. To delete a node from the tree.\n4. To print the inorder travesal of tree.\n5. To print the preorder traversal of the tree.\n6. To print the postorder traversal of the tree.\n7. To exit.\n");
		scanf("%d", &choice);
		switch(choice)
		{
			case 1:
				printf("Enter the value you want to insert\n");
				scanf("%d", &value);
				root = insert(root, value);
				break;
			case 2:
				printf("Enter the value you want to search.\n");
				scanf("%d", &value);
				if(search(root, value))
					printf("The value %d is found :-)\n", value);
				else if(!search(root, value))
					printf("Not found :'-(\n");
				break;
			case 3:
				printf("Enter the value you want to delete.\n");
				scanf("%d", &value);
				root = delete(root, value);
				break;
			case 4:
				printf("The inorder traversal of the tree is :-\n");
				inorder(root);
				printf("\n");
				break;
			case 5:
				printf("The preorder traversal of the tree is :-\n");
				preorder(root);
				printf("\n");
				break;
			case 6:
				printf("The postorder traversal of the tree is :-\n");
				postorder(root);
				printf("\n");
				break;
			case 7:
				condition = False;
				break;
			default:
				printf("Enter a valid choice between %d and %d (both included).\n", 1, 6);
				break;
		}
	}
	return 0;
}
struct Node* newNode(int value)
{
	struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
	temp -> data = value;
	temp -> left = NULL;
	temp -> right = NULL;
	return temp;
}
struct Node* insert(struct Node* root, int value)
{
	if(root == NULL)
	{
		root = newNode(value);
		return root;
	}
	else
	{
		if(value < root -> data)
			root -> left = insert(root -> left, value);
		else if(value > root -> data)
			root -> right = insert(root -> right, value);
		else
		{
			printf("Value already exists!\n");
			return root;
		}
	}
	return root;
}
int search(struct Node* root, int value)
{
	if(root == NULL)
		return False;
	else
	{
		if(root -> data == value)
			return True;	
		else if(root -> data > value)
			return search(root -> left, value);
		else if(root -> data < value)
			return search(root -> right, value);
	}	
}
void inorder(struct Node* root)
{
	if(root == NULL)
		return;
	else
	{
		inorder(root -> left);
		printf("%d -> ", root -> data);
		inorder(root -> right);
	}
}
void preorder(struct Node* root)
{
	if(root == NULL)
		return;
	else
	{
		printf("%d -> ", root -> data);
		preorder(root -> left);
		preorder(root -> right);
	}
}
void postorder(struct Node* root)
{
	if(root == NULL)
		return;
	else
	{
		postorder(root -> left);
		postorder(root -> right);
		printf("%d -> ", root -> data);
	}
}
struct Node* minimum(struct Node* root)
{
	struct Node* temp = root;
	while(temp != NULL && temp -> left != NULL)
		temp = temp -> left;
	return temp;
}
struct Node* delete(struct Node* root, int value)
{
	if(root == NULL)
		return root;
	if(root -> data == value)
	{
		struct Node* temp = (struct Node*)malloc(sizeof(struct Node*));
		if(root -> left == NULL)
		{
			temp = root -> right;
			free(root);
			return temp;
		}
		else if(root -> right == NULL)
		{
			temp = root -> left;
			free(root);
			return temp;
		}
		else
		{
			temp = minimum(root -> right);
			root -> data = temp -> data;
			root -> right = delete(root -> right, temp -> data);
		}
	}
	else if(root -> data > value)
		root -> left = delete(root -> left, value);
	else if(root -> data < value)
		root -> right = delete(root -> right, value);
	return root;
}
