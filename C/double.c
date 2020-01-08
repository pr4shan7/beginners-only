#include<stdio.h>
#include<stdlib.h>

void create();
void traverse();
void inverse();

struct node
{
    int info;
    struct node *ll,*rl;
};

struct node *first = NULL;

int main()
{
    int n,i;
    printf("Enter number of terms in Link list ");
    scanf("%d",&n);
    for (i=0;i<n;i++)
    {
        create();
    }
    traverse();
    inverse();
}

void create()
{
    int n;
    struct node *ptr,*cpt;
    ptr = (struct node*) malloc(sizeof(struct node));
    printf("Enter the term ");
    scanf("%d",&n);
    
    if (first == NULL)
    {
        first = ptr;
        ptr -> rl = NULL;
        ptr -> ll = NULL;
        ptr -> info = n;
    }
    else
    {
        cpt = first;
        while (cpt -> rl != NULL)
        {
            cpt = cpt -> rl;
        }
        cpt->rl=ptr;
        ptr->info=n;
        ptr->rl=NULL;
        ptr->ll=cpt;
    }
}

void traverse()
{
    struct node *ptr;
    ptr = first;
    printf("Traversing of list is ");
    while (ptr->rl != NULL )
    {
        printf("%d ",ptr->info);
        ptr = ptr -> rl;
    }
    printf("%d\n",ptr -> info);
}

void inverse()
{
    struct node *ptr;
    ptr = first;
    printf("Inverse traversing of list is ");
    while (ptr->rl !=NULL)
    {
        ptr=ptr->rl;
    }
    while (ptr->ll != NULL)
    {
        printf("%d ",ptr->info);
        ptr = ptr -> ll;
    }
    printf("%d\n",ptr -> info);
}
