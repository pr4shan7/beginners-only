#include<stdio.h>
#include<stdlib.h>

void create();
void traverse();
void insert();
void delete();
void search();

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
    for (i=0;i<n;i++)
    {
        create();
    }
    traverse();
    insert();
    traverse();
    delete();
    traverse();
    search();
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

void traverse()
{
    struct node *ptr;
    ptr = first;
    printf("Traversing of list is ");
    while (ptr->link != NULL )
    {
        printf("%d ",ptr->info);
        ptr = ptr -> link;
    }
    printf("%d\n",ptr -> info);
}

void insert()
{
    struct node *ptr,*cpt,*tpt;
    int i,m,n;
    ptr = (struct node*) malloc(sizeof(struct node));
    printf("Enter the term ");
    scanf("%d",&n);
    printf("Enter the position of term ");
    scanf("%d",&m);
    cpt=first;
    if ( m == 0 )
    {
        ptr->info=n;
        ptr->link=first;
        first = ptr;
    }
    else
    {
        for(i=1;i<m-1;i++)
        {
            cpt=cpt->link;
        }
        ptr->info = n;
        ptr->link = cpt->link;
        cpt->link = ptr;
    }
}
void delete()
{
    struct node *cpt,*tpt;
    int i,m;

    printf("Enter the position of term ");
    scanf("%d",&m);
    cpt=first;
    if ( m ==0 )
    {
        first = cpt->link;
        free(cpt);
    }
    else
    {
        for(i=1;i<m-1;i++)
        {
            cpt=cpt->link;
        }
        tpt=cpt->link;
        cpt->link=cpt->link->link;
        free(tpt);
    }
}

void search()
{
    struct node *ptr;
    int i,n=0,m;
    printf("Enter the term to search from link list ");
    scanf("%d",&m);
    ptr = first;
    while(ptr->link != NULL)
    {
        n++;
        if (ptr->info == m)
        {
            printf("%d is in the %d node\n",m,n);

        }
        ptr=ptr->link;
    }
}
