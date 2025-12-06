'''
3578. Count partitions With Max-Min Difference at Most K

You are given an integer array nums and an integer k. Your task is to partition nums into one or more non-empty contiguous segments such that in each segment, the difference between its maximum and minimum elements is at most k.

Return the total number of ways to partition nums under this condition.

Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [9,4,1,3,7], k = 4

Output: 6

Explanation:

There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most k = 4:

[[9], [4], [1], [3], [7]]
[[9], [4], [1], [3, 7]]
[[9], [4], [1, 3], [7]]
[[9], [4, 1], [3], [7]]
[[9], [4, 1], [3, 7]]
[[9], [4, 1, 3], [7]]
Example 2:

Input: nums = [3,3,4], k = 0

Output: 2

Explanation:

There are 2 valid partitions that satisfy the given conditions:

[[3], [3], [4]]
[[3, 3], [4]]
 

Constraints:

2 <= nums.length <= 5 * 104
1 <= nums[i] <= 109
0 <= k <= 109
'''


#solution:
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        left, cnt, mod_ = 0, 1, 1_000_000_007
        mnQueue, mxQueue, dp = deque(), deque(), [cnt]
        
        for rght, num in enumerate(nums):
            while mxQueue and num > nums[mxQueue[-1]]:
                mxQueue.pop()
            while mnQueue and num < nums[mnQueue[-1]]:
                mnQueue.pop()

            mxQueue.append(rght)    
            mnQueue.append(rght)

            while nums[mxQueue[0]] - nums[mnQueue[0]] > k:
                cnt-= dp[left]
                left+= 1
                
                if left > mnQueue[0]: mnQueue.popleft()
                if left > mxQueue[0]: mxQueue.popleft()

            dp.append(cnt)
            cnt*= 2
            cnt%= mod_

        return dp[-1] %mod_
