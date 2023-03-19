# Count Number of Inversions in Given Array

In this problem, you are `given an array` in `unsorted order`. You have to count the number of inversions i.e. the number of instances where `i<j` but `A[i] > A[j]`.

Try to do it time `O(n log (n) )`

Input: 
> The `number of elements` in the array.
>
> `The array`.

Output:
> The `number of inversions`.
>
---

### Examples:

Input:
> 4
>
> 1 2 3 4

Output:
> 0

Explanation:
The input is sorted.

Input:
> 4
>
> 8 4 2 1

Output:
> 6

Explanation:
The inversions are :(8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).

Input:
>5
>
>1 20 6 4 5

Output:
>5

Explanation: 
The inversions are : (20, 6), (20, 4), (20, 5), (6, 4), (6, 5). 