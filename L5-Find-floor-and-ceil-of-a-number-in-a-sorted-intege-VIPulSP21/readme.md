# Find floor and ceil of a number in a sorted integer array

Given a sorted integer array, find the floor and ceil of a given number in it. 

For a number `x`, `floor(x)` is the largest integer in the array less than or equal to `x`, and `ceil(x)` is the smallest integer in the array greater than or equal to `x`. If the floor or ceil doesn’t exist, consider it to be `-1`. 

For example,

Input: 
        
        6
        
        1 4 9 16 25 34  
      
        1

Output :

         1 1

Explaination: 1 is present in this array. So, `floor(1) = ceil(1) = 1`

Input:
      6
      
      1 4 9 16 25 34

      18

Output:

      16 25
      
         
Input : 

       6
       
       1 4 9 16 25 34
       
       0

Output : 

        -1 1

Explaination: `0` is smaller than all the elements in the array. So, `floor(0) = -1`. And, `ceil(0) = 1`.

Input :

       6
       
       1 4 9 16 25 34
       
       35

Output : 

         34 -1

After you have stored the input in the array, the running time of your algorithm should be `O(log n)`