/* 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。 
*/

// 题目利用双指针缩小搜索空间 —— 去重部分参考题解pinku-2
// 时间，快排O(logN)，搜索为O(n^2)，故O(n^2)，空间：原址排序，所以不需要额外空间，O(1)

#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {

        int n = nums.size();
        // 边界条件
        if (n < 3) return 0;
        if (n == 3) return (nums[0] + nums[1] + nums[2]);
        // 快排
        quickSort(nums, 0, n - 1);
        // 返回值初始化
        int res = nums[0] + nums[1] + nums[2];

        for (int i = 0; i <= n - 3; i++)
        {
            int l = i + 1, r = n - 1;
            while (l < r)
            {
                int lNum = nums[l], rNum = nums[r];
                int sum = nums[i] + lNum + rNum;
                // 如果新求和结果比之前的更接近target，更新返回值
                if (abs(sum - target) < abs(res - target))
                {
                    res = sum;
                }
                // 根据求和结果更新左右指针
                if (l < r && sum > target)
                {
                    // 去重
                    while (l < r && nums[r] == rNum) --r;
                }
                else
                {
                    while (l < r && nums[l] == lNum) ++l;
                }
            }
            // 判断原始nums序列中，index下标是否有重复数字，如果有跳过
            while (i + 1 <= n - 3 && nums[i] == nums[i + 1]) ++i;
        }
        return res;
    }

    void quickSort(vector<int>& nums, int left, int right)
    {
        if (left < right)
        {
            int index = partition(nums, left, right);
            quickSort(nums, left, index - 1);
            quickSort(nums, index + 1, right);
        }
    }

    int partition(vector<int>& nums, int left, int right)
    {
        int pivot = nums[left];
        int l = left, r = right;
        while (l < r)
        {
            while (l < r && nums[r] >= pivot) r--;
            nums[l] = nums[r];
            while (l < r && nums[l] <= pivot) l++;
            nums[r] = nums[l];
            nums[l] = pivot;
        }
        return l;
    }
};
