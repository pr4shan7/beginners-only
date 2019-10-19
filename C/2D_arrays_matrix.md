An array of arrays is known as 2D array. The two dimensional (2D) array in C programming is also known as matrix. A matrix can be represented as a table of rows and columns. Before we discuss more about two Dimensional array lets have a look at the following C program.


initialization of 2D Array:
There are two ways to initialize a two Dimensional arrays during declaration.


int disp[2][4] = {
    {10, 11, 12, 13},
    {14, 15, 16, 17}
};
OR
int disp[2][4] = { 10, 11, 12, 13, 14, 15, 16, 17};
Although both the above declarations are valid, I recommend you to use the first method as it is more readable, because you can visualize the rows and columns of 2d array in this method.


To store data:
To store the elements entered by user we are using two for loops, one of them is a nested loop. The outer loop runs from 0 to the (first subscript -1) and the inner for loops runs from 0 to the (second subscript -1). This way the the order in which user enters the elements would be abc[0][0], abc[0][1], abc[0][2]…so on.

#include<stdio.h>
int main(){
   /* 2D array declaration*/
   int abc[5][4];
   /*Counter variables for the loop*/
   int i, j;
   for(i=0; i<5; i++) {
      for(j=0;j<4;j++) {
         printf("Enter value for abc[%d][%d]:", i, j);
         scanf("%d", &abc[i][j]);
      }
   }
   return 0;
}

