#include <stdio.h>
#include <math.h>
int main()
{ /*An arithmetic progression (AP) or arithmetic sequence is a sequence of numbers 
    such that the difference between the consecutive terms is constant.
    Like 5,7,9,11,13 all of these have a difference of 2 between two consecutive terms. */
     int a, d, n, i, tn;
     int sum = 0; 
     printf("Enter the first term value of the A.P. series: ");      
     scanf("%d", &a);
     printf("Enter the total numbers in the A.P. series: ");
     scanf("%d", &n);
     printf("Enter the common difference of A.P. series: ");
     scanf("%d", &d);
     sum = (n * (2 * a + (n - 1)* d ))/ 2;//to calcutate the sum of elements of an A.P.Sum=a+(a+d)+(a+2d)+...and soon. 
     tn = a + (n - 1) * d;//to calculate n th term of an A.P.
     printf("Sum of the A.P series is: ");
     for (i = a; i <= tn; i = i + d )
     {
          if (i != tn)
               printf("%d + ", i);
          else
               printf("%d = %d ", i, sum);
     }
     return 0;
}
