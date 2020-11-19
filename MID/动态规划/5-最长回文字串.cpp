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
        int n = s.size();
        vector<char> revStr(n);
        for (int i = 0; i < n; i++)
        {
            revStr[i] = s[n - i - 1];
        }
        int left = 0, right = 0;
        int res = 0;
        while (right < n)
        {

        }
    }
};