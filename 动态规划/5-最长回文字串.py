""" 
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        # 中心扩展
        # 判断边界条件
        if n == 0:
            return ""
        
        def extend(i: int, j: int, s: str) -> str:
            while (i >= 0 and j < len(s) and s[i] == s[j]):
                i -= 1
                j += 1
                return s[i + 1 : j]

        max_len = 1
        tmp = s[0]
        for i in range(n - 1):
            e1 = extend(i, i, s)
            e2 = extend(i, i + 1, s)
            max_e = max(len(e1), len(e2))
            if max_e >= max_len:
                max_len = max_e
                tmp = e1 if len(e1) > len(e2) else e2
        return tmp