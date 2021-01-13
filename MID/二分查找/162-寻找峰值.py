"""
峰值元素是指其值大于左右相邻值的元素。
给你一个输入数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
你可以假设 nums[-1] = nums[n] = -∞ 。
输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2。
"""
from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while (left < right):
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left