/* 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。 */

#include<iostream>
#include<string>
#include<vector>

using namespace std;


class Solution {
public:
    string longestPalindrome(string s) {
        // DP方法 时间复杂度O(n^2)，空间O(n^2)
        int n = s.size();
        vector< vector<int> > dp(n, vector<int>(n));
        string ans;

        // 通过 l 判断回文字串判断时的长度
        for (int l = 0; l < n; ++l)
        {
            // 从第一个 字符 开始判断
            for (int i = 0; i + l < n; ++i)
            {
                // 回文字串的末尾字符
                int j = i + l;
                // 如果回文字串的长度为1，只有1个字符，则肯定为回文，值为1
                if (l == 0) dp[i][j] = 1;
                // 如果回文字串的长度为2，则需要判断首尾两个字符是否相等
                else if (l == 1) dp[i][j] == (s[i] == s[j]);
                // 其他长度下，通过DP，返回，缩小长度后的字串是否为回文，同时该长度下首尾字符是否相等
                else dp[i][j] = (dp[i + 1][j - 1] && s[i] == s[j]);
                // 如果该长度下是回文字串同时该字串长度比算法返回字符串ans中的长度长，则更新返回值为新的字串
                if (dp[i][j] && l + 1 > ans.size()) ans = s.substr(i, l + 1);
            }
        }
        return ans;
    }
};