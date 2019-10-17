"""Binary search function using an iterative approach.
The function takes two inputs: a Python list to search through, 
and the values you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    min = 0
    max = len(input_array)
    while True:
        length = max - min
        # find the midpoint
        if length % 2 == 1: 
            mid = min + length / 2
        else:
            mid = min + (length + 1) / 2
        if value == input_array[mid-1]:
            return mid - 1
        if value > input_array[mid-1]:
            min = mid
        else:
            max = mid
        if length == 1:
            return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
