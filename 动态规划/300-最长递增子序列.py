"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

时空复杂度：O(n^2)  O(n)
"""
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums: return 0
        """
        # 时间复杂度太高
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)
 """
        tail = [0] * len(nums)
        res = 0
        
        for num in nums:
            left = 0
            right = res
            while left < right:
                mid = (left + right) // 2
                if tail[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            tail[left] = num
            # 当前面找到有更小的值时，除了更新left去继续查找之外，需要更新tail的长度，通过 right 和 res 的值比较
            if right == res: res += 1
        return res
