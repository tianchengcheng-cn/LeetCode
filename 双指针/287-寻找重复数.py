"""
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。
假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。

示例 1：
输入：nums = [1,3,4,2,2]
输出：2
参考解析：
https://leetcode-cn.com/problems/find-the-duplicate-number/solution/miao-dong-kuai-man-zhi-zhen-by-wo-you-dian-ben/
https://blog.csdn.net/LittleNyima/article/details/105349081
时空复杂度：O(n), O(1)
"""
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while (slow != fast):
            slow = nums[slow]
            fast = nums[nums[slow]]
        # 注意，环入口不一定是重复数字，如链接2示例。相当于值是快指针比慢指针夺走了k个环而以，需要考虑重复数字之间的距离。故不一定是重复数字为入口
        # 因此，需要再次搜索重复数字。个人觉得可以理解为，通过快慢指针识别环，通过环分割数据，减小判断量
        root = 0
        while (root != slow):
            root = nums[root]
            slow = nums[slow]
        return slow