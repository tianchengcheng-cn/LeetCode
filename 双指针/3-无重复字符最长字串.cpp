/* 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。 */
#include<iostream>
#include<string>
#include<unordered_map>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left = 0, right = 0;
        int res = 0;
        unordered_map<char, int> window;
        while (right < s.size())
        {
            char push = s[right];
            right++;
            window[push]++;
            // 当window中该字符个数超过1时，表示出现重复字符，开始更新左边界
            while (window[push] > 1))
            {
                char pop = s[left];
                left++;
                window[pop]--;
            }
            res = max(res, right - left);
        }
        return res;
    }
};