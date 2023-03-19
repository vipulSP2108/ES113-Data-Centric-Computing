# Find an element in an almost sorted array

Suppose you are given an almost sorted array i.e. the elements of the array are monotonic increasing and then decreasing e.g. 2, 4, 6, 7, 5, 1.

Input the size of the array, the array and the element to search.

### Examples:

Input: 

       5

       10 20 30 35 25

       20


Output: 

      1


Input: 

       5

       10 20 30 35 25

       70


Output: 

      -1

After you have stored in the input, the running time of your algorithm should be `O(log n)`.