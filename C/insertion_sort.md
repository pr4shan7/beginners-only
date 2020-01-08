Insertion sort is a sorting algorithm in which the elements are transferred one at a time to the right position.
In other words, an insertion sort helps in building the final sorted list, one item at a time, with the movement
of higher-ranked elements. An insertion sort has the benefits of simplicity and low overhead.

In an insertion sort, the first element in the array is considered as sorted, even if it is an unsorted array. 
In an insertion sort, each element in the array is checked with the previous elements, resulting in a growing 
sorted output list. With each iteration, the sorting algorithm removes one element at a time and finds the
appropriate location within the sorted array and inserts it there. The iteration continues until the whole list is sorted.
There are many advantages associated with an insertion sort. It is simple to implement and is quite efficient for small
sets of data, especially if it is substantially sorted. It has low overhead and can sort the list as it receives data.
Another advantage associated with insertion sort is the fact that it needs only a constant amount of memory space for
the whole operation. It is more efficient than other similar algorithms such as bubble sort or selection sort.
However, an insertion sort is less efficient on larger data sets and less efficient than the heap sort or quick
sort algorithms.

Example:<br>
12, 11, 13, 5, 6<br>
Let us loop for i = 1 (second element of the array) to 4 (last element of the array)<br>
i = 1. Since 11 is smaller than 12, move 12 and insert 11 before 12<br>
11, 12, 13, 5, 6<br>
i = 2. 13 will remain at its position as all elements in A[0..I-1] are smaller than 13<br>
11, 12, 13, 5, 6<br>
i = 3. 5 will move to the beginning and all other elements from 11 to 13 will move one position ahead of their current position.<br>
5, 11, 12, 13, 6<br>
i = 4. 6 will move to position after 5, and elements from 11 to 13 will move one position ahead of their current position.<br>
5, 6, 11, 12, 13 <br>

(Reference - geeksforgeeks.org for example case) 
