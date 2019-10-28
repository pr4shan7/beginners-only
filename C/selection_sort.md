Selection sort is a simple sorting algorithm. This sorting algorithm is an in-place comparison-based algorithm 
in which the list is divided into two parts, the sorted part at the left end and the unsorted part at the right
end. Initially, the sorted part is empty and the unsorted part is the entire list.

The smallest element is selected from the unsorted array and swapped with the leftmost element, and that element
becomes a part of the sorted array. This process continues moving unsorted array boundary by one element to the
right.

This algorithm is not suitable for large data sets as its average and worst case complexities are of Ο(n2), where
n is the number of items.

Example:<br>

arr[] = 64 25 12 22 11<br>

// Find the minimum element in arr[0...4]<br>
// and place it at beginning of arr[0...4]<br>
11 25 12 22 64<br>

// Find the minimum element in arr[1...4]<br>
// and place it at beginning of arr[1...4]<br>
11 12 25 22 64<br>

// Find the minimum element in arr[2...4]<br>
// and place it at beginning of arr[2...4]<br>
11 12 22 25 64<br>

// Find the minimum element in arr[3...4]<br>
// and place it at beginning of arr[3...4]<br>
11 12 22 25 64 <br>


(Reference - geeksforgeeks.org for example case) 
