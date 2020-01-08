Linear search is used on a collections of items. It relies on the technique of traversing a list from start
to end by exploring properties of all the elements that are found on the way.

For example, consider an array of integers of size __N__.
You should find and print the position of all the elements with value __x__. Here, the linear search is based on
the idea of matching each element from the beginning of the list to the end of the list with the integer __x__, 
and then printing the position of the element if the condition is `True'.

The time complexity of above algorithm is O(n).
Linear search is rarely used practically because other search algorithms such as the binary search algorithm
and hash tables allow significantly faster searching comparison to Linear search.

Example:<br>

Consider an array,<br>
arr[]=[0,1,2,3,4,5,6,7,8,9]

If you want to determine the positions of the occurrence of the number **7** in this array. To determine the 
positions, every element in the array from start to end, i.e., from index **1** to index **10** will be compared with 
number **7** , to check which element matches the number **7**.
