# Given an integer array nums return the number of Strange pairs in the array.

A `Strange pair` is a pair `(i,j)` such that: `i<j` and  `nums[i]>2*nums[j]`.

Input: 
> The `number of elements` in the array.
>
> `The array`.

Output:
> `Number of strange pairs`.
>
---

### Examples:
Input: 
> 5 
>
> 1 3 2 3 1

Output:
2

Explanation:
>
>The strange pairs are:
>
>`(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1`
>
>`(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1`
