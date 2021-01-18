"""
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
"""

from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0: return 0
        if size == 1: return nums[0]

        p = nums[0]
        maxP = nums[0]
        minP = nums[0]
        for i in range(1, size):
            temp = maxP
            maxP = max(max(maxP * nums[i], nums[i]), minP * nums[i])
            minP = min(min(temp * nums[i], nums[i]), minP * nums[i])
            p = max(maxP, p)
        return p