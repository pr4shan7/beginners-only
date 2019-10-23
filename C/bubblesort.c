//code for bubble sort implementation

#include <stdio.h>
 
int main()
{
  int Unsorted_Array[1000], size_of_array, Loop1_Counter, Loop2_Counter, swap_variable;
 
  printf("Please enter the number of elements\n");
  scanf("%d", &size_of_array);
  printf("Enter the integers to be sorted\n");
 
  for (Loop1_Counter = 0; Loop1_Counter < size_of_array; Loop1_Counter++)
    scanf("%d", &Unsorted_Array[Loop1_Counter]);							//input array
 
  for (Loop1_Counter = 0 ; Loop1_Counter < size_of_array - 1; Loop1_Counter ++)				//1st Loop for Counter
  {
    for (Loop2_Counter = 0 ; Loop1_Counter < size_of_array - Loop1_Counter - 1; Loop2_Counter ++)	//2nd Loop for Swap
    {
      if (Unsorted_Array[Loop2_Counter] > Unsorted_Array[Loop2_Counter + 1])  				// For descending order use <
      {
        swap_variable = Unsorted_Array[Loop2_Counter];							// code to swap values
        Unsorted_Array[Loop2_Counter]   = Unsorted_Array[Loop2_Counter + 1];
	Unsorted_Array[Loop1_Counter + 1] = swap_variable;
      }
    }
  }
 
  printf("Sorted array in ascending order:\n");
 
  for (Loop1_Counter = 0; Loop1_Counter < size_of_array; Loop1_Counter ++)
     printf("%d\n", Unsorted_Array[Loop1_Counter]);							// output sorted array
 
  return 0;
}

