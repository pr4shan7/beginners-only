
#include<bits/stdc++.h>
using namespace std;

struct bst{

	int data;
	struct bst* left;
	struct bst* right;
};

typedef struct bst node;

set< int > s;

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

node* commonAncestor(node* root,int p,int q){

	if(root==NULL)
		return;

	if(root->data < p && root->data < q)
		return commonAncestor(root->right,p,q);
	else if(root->data > p && root->data > q)
		return commonAncestor(root->left,p,q);
	else
		return  root;
}

void search(node* root,int x){

	if(root==NULL)
		return;

	s.insert(root->data);

	if(root->data==x)
		return;
	else if(root->data >x)
		search(root->left,x);
	else
		search(root->right,x);
}

int main()
{	
	int n,num,i,p,q;
	cin >> n;
	node* root=NULL;

	for(i=0;i<n;i++)
	{
		cin >> num
		insert(&root,num);
	}

	cin >> p >> q;

	node* common=commonAncestor(root,p,q);

	search(common,p);
	search(common,q);

	cout << *(s.end()-1);

}
