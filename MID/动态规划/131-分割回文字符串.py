"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。
输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def centerSpread(left, right):
            while 0 <= left and right < size and s[left] == s[right]:
                dp[left][right] = True
                left -= 1
                right += 1

        def recall(s, size, start, subset):
            if start == size:
                res.append(subset[:])
                return
            for i in range(start, size):
                # print(i)
                if not dp[start][i]:
                    # print('j')
                    continue
                subset.append(s[start:i+1])
                recall(s, size, i + 1, subset)
                # print('b_pop - >', subset)
                # print('res: ', res)
                subset.pop()
                # print('a_pop -> ', subset)



        res = []
        size = len(s)
        dp = [[False for _ in range(size)] for _ in range(size)]
        print(dp)
        for i in range(size):
            centerSpread(i, i)
            centerSpread(i, i + 1)
        print(s)
        print(dp)
        recall(s, size, 0, [])
        print(res)

if __name__ == "__main__":
    s = 'baa'
    S_ = Solution()
    S_.partition(s)