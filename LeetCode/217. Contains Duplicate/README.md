217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 
Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109


Personal Notes:

If I compare each item with all the other items of the list then the time complexity becomes **O(n2)**

If I use nums.sort() and then comapare with adjacent item, then the time complexity becomes **O(nlogn)** and space complexity becomes **O(1)**

In above solution, the time complexity becomes **O(n)**, even though the space complexity becomes **O(n)** too.




