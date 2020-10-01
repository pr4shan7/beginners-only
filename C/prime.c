#include<stdio.h>
int main(){
    int number,i,flag=0;
    printf("Ener the number you want to check");
    scanf("%d",&number);
    for(i=2;i<number;i++){
        if(number%i==0){
            flag=1;            
        }
    }
    if(flag!=1){
        printf("%d is a prime number",number);
    }
    else
    {
        printf("Not a prime number");
    }
    
}