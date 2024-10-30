238. Product of Array Except Self

Given an integer array nums, return an array answer such that *answer[i]* is equal to the product of all the elements of nums except *nums[i]*.

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in **O(n)** time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]

Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]

Output: [0,0,9,0,0]

 

Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

Personal Note:

Using division, the problem can be solved in **O(n)** time complexity and **O(1)** space complexity. But the problem explicitly states to not use division.

So, using prefix and postfix, the problem is solved in **O(n)** time complexity and **O(1)** space complexity since the output array doesn't count as extra space.
