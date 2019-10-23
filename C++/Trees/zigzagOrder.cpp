
#include<bits/stdc++.h>
using namespace std;

struct bst{

	int data;
	struct bst* left;
	struct bst* right;
};

typedef struct bst node;

void insert(node** root_ref,int x)
{

	if(*root_ref==NULL){
		node* temp=(node*)malloc(sizeof(node));
		temp->data=x;
		temp->left=NULL;
		temp->right=NULL;
		*root_ref=temp;
		 return;
		}
	

	else if(x<(*root_ref)->data)
		insert(&((*root_ref)->left),x);

	else
		insert(&((*root_ref)->right),x);

}


int main()
{	
	int n,num,i;
	scanf("%d",&n);
	node* root=NULL;

	for(i=0;i<n;i++)
	{
		scanf("%d",&num);
		insert(&root,num);
	}

	vector<vector<int> > v;
	vector<int> temp1;
	stack<node*> curr,next;
	
	curr.push(root);
	int leftToRight=0;

	while(!curr.empty()){
		node* temp=curr.top();
		curr.pop();

		temp1.push_back(temp->data);
		if(leftToRight){
			if(temp->right)
				next.push(temp->right);
			if(temp->left)
				next.push(temp->left);
		}

		else{
			if(temp->left)
				next.push(temp->left);
			if(temp->right)
				next.push(temp->right);
		}

		if(curr.empty()){
			v.push_back(temp1);
			temp1.clear();
			leftToRight=1-leftToRight;
			swap(curr,next);
		}
	}


}