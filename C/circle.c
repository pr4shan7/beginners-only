#include<stdio.h>
#include<stdlib.h>

void create();
void traverse(int n);
void circle();

struct node
{
    int info;
    struct node *link;
};

struct node *first=NULL;
int main()
{
    int n,i;
    printf("Enter number of terms in Link list ");
    scanf("%d",&n);
    for (i=0;i<n-1;i++)
    {
        create();
    }
    circle();
    traverse(n);
}

void create()
{
    struct node *ptr, *cpt;
    int n;
    ptr = (struct node*) malloc(sizeof(struct node));
    printf("Enter the term ");
    scanf("%d",&n);
    if(first==NULL)
    {
        first = ptr;
        ptr -> info = n;
        ptr -> link = NULL;
    }
    else
    {
        cpt=first;
        while(cpt->link!=NULL)
        {
            cpt=cpt->link;
        }
        cpt->link=ptr;
        ptr->info=n;
        ptr->link=NULL;
    }
}

void traverse(int n)
{
    int i;
    struct node *ptr;
    ptr = first;
    printf("Traversing of list is ");
    for (i=0;i<n;i++)
    {
        printf("%d ",ptr->info);
        ptr = ptr -> link;
    }
    printf("%d\n",ptr -> info);
}

void circle()
{
    struct node *ptr,*cpt;
    int n;
    printf("Enter the last term ");
    scanf("%d",&n);
    ptr = (struct node*) malloc(sizeof(struct node));
    cpt = first;
    while(cpt->link!=NULL)
    {
        cpt = cpt->link;
    }
    cpt->link=ptr;
    ptr->info = n;
    ptr->link = first;
}
