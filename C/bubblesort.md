Bubble sort is a sorting algorithm, used to sort an array of numbers into ascending or descending order.
Although it is relatively less efficient and time complexity of worst case is quite high, it is useful to understand bubble sort as a starting to understand how sorting works.

Bubble sort is a swapping algorithm that swaps adjacent elements in case they are in the wrong order.
It uses two loops for this process. The first loop begins from the 0th element, till the 2nd last, or (size - 1)th element. It is the counter for how many times the 2nd loop has to iterate in worst case.
The 2nd Loop starts from the 0th element till the (size - 1 - 1st-loop-counter)th element. Here, size - 1 is used to prevent overflow of array, while the initial counter is subtracted to reduce redundancy in the loop, as in each iteration of the 1st loop, the largest/smallest element gets sorted to the end of the array, and thus doesn't have to be considered for subsequent operations.

Example:
First Pass:
( 5 1 4 2 8 ) –>  ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
( 1 4 2 5 8 ) –>  ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.

Second Pass:
( 1 4 2 5 8 ) –>  ( 1 4 2 5 8 )
( 1 4 2 5 8 ) –>  ( 1 2 4 5 8 ), Swap since 4 > 2
( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.

Third Pass:
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )

(Reference - geeksforgeeks.org for example case) 
