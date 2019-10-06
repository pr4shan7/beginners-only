//code for bubble sort implementation

#include <stdio.h>
 
int main(void)
{
  int unsorted_array[1000], size, i, j, swap;
 
  printf("Please enter the number of elements\n");
  scanf("%d", &size);
  printf("Enter the integers to be sorted\n");
 
  for (i = 0; i < size; i++)
    scanf("%d", &unsorted_array[i]);		//input array
 
  for (i = 0 ; i < size - 1; i++)		//outer loop
  {
    for (j = 0 ; j < size - i - 1; j++)		// inner loop
    {
      if (unsorted_array[j] > unsorted_array[j+1])  		// For descending order use <
      {
        swap       = unsorted_array[j];			// code to swap values
        unsorted_array[j]   = unsorted_array[j+1];
        unsorted_array[j+1] = swap;
      }
    }
  }
 
  printf("Sorted array in ascending order:\n");
 
  for (i = 0; i < size; i++)
     printf("%d\n", unsorted_array[i]);		// output sorted array
 
  return 0;
}

