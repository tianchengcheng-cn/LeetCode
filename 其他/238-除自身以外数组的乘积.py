"""
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

输入: [1,2,3,4]
输出: [24,12,8,6]

代码来自：https://leetcode-cn.com/problems/product-of-array-except-self/solution/product-of-array-except-self-shang-san-jiao-xia-sa/
时空复杂度：O(n), O(1)
"""
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, p, q = [1], 1, 1
        # 注意，range中的值为 len(nums) - 1，表示最后一个不计算，即排除最后一个自身相乘
        for i in range(len(nums) - 1):
            p *= nums[i]
            res.append(p)
        # 注意，res中的下标为 i - 1，表示最后一个乘1，即不做修改，从倒数第二个修改乘q
        for i in range(len(nums) - 1, 0, -1):
            q *= nums[i]
            res[i - 1] *= q
        return res