'''
1262. Greatest Sum Divisible By Three

Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.

 

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 

Constraints:

1 <= nums.length <= 4 * 104
1 <= nums[i] <= 104
'''

#solution:

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        sum_ = 0

        min1 = min2 = float('inf')
        min11 = min22 = float('inf')

        for x in nums:
            sum_ += x
            r = x % 3

            if r == 1:
                if x < min1:
                    min11, min1 = min1, x
                elif x < min11:
                    min11 = x
            elif r == 2:
                if x < min2:
                    min22, min2 = min2, x
                elif x < min22:
                    min22 = x

        rem = sum_ % 3

        if rem == 0:
            return sum_

        if rem == 1:
            r1 = min1
            r2 = min2 + min22 if min2 < float('inf') and min22 < float('inf') else float('inf')
            remove = min(r1, r2)
            return 0 if remove == float('inf') else sum_ - remove
        else:
            r1 = min2
            r2 = min1 + min11 if min1 < float('inf') and min11 < float('inf') else float('inf')
            remove = min(r1, r2)
            return 0 if remove == float('inf') else sum_ - remove
