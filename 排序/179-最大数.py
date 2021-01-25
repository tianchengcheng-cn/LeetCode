"""
给定一组非负整数 nums，重新排列它们每个数字的顺序（每个数字不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

输入：nums = [3,30,34,5,9]
输出："9534330"



时空复杂度：O(nlogn)，O(n)
"""
from typing import List

class LargeKey(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 自定义排序
        largeNums = "".join(sorted(map(str, nums), key=LargeKey))
        # 如果数组中只包含0，则输出“0”即可，不需要“000”，否则正常输出
        return "0" if largeNums[0] == "0" else largeNums
