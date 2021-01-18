/* 参考题解：nettee题目中的解答
指针每一次移动，意味着排除掉了一个柱子。比如固定左边，右边每次j--，则盛得水减少，循环i++和j--，则会将整个空间进行搜索 */

// 题目利用双指针缩小搜索空间
// 时间O(n)，空间O(1)

#include<iostream>
#include<vector>

using namespace std;

int maxArea(vector<int>& height)
{
    int i = 0, j = height.size() - 1;
    int ans = 0;
    while (i < j)
    {
        // 选择较短的柱子作为高，为本次的盛水量
        int area = (j - i) * min(height[i], height[j]);
        // 更新返回值
        ans = max(ans, area);
        // 选择短柱子一侧进行收缩
        if (height[i] < height[j]) i++;
        else j--;
    }
    return ans;
}
