#include<stdio.h>
int main(){
    int a,b,i;
    printf("Enter a");
    scanf("%d", &a);
    printf("Enter b");
    scanf("%d", &b);
    for(i=(a>b?b:a);i>1;i--){
        if(a%i==0 && b%i==0){
            printf("HCF is %d",i);
            break;
        }
    }
}