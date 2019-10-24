#include<stdio.h>
void swap(int *pa,int *pb)
{
 int temp=pa;
 pa=pb;
 temp=pb;
}

int main()
{
 int a,b;
 
 scanf("%d %d",&a,&b);
 swap(&a,&b);
 printf("%d %d\n",a,b);
 
 return 0;
}
