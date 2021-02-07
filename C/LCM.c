#include<stdio.h>
int main() {
   int a, b,i;
   printf("Enter a");
   scanf("%d",&a);
   printf("Enter b");
   scanf("%d",&b);
   for(i=(a>b?a:b);i<=(a*b);i=i+(a>b?a:b)){
       if(i%a==0 && i%b==0){
           break;
       }
   } 
   printf("LCM is %d", i);
}