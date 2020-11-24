/* 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
 */

// 题目利用双指针缩小搜索空间 —— 去重部分参考题解pinku-2
// 时间O(n^2)，空间：原址排序，所以不需要额外空间，单变量为O(1)级别，答案返回ans为O(3k)级别，k为集合中列表个数，总O(k)

#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    vector< vector<int> > threeSum(vector<int>& nums)
    {
        // 排序 + 双指针
        // 快排
        int n = nums.size();
        partition(nums, 0, n - 1);
        // 双指针判断
        vector< vector<int> > ans;
        for (int i = 0; i <= n - 3; ++i)
        {
            // 固定i，判断i右侧窗口是否有满足条件的两个数值
            int target = 0 - nums[i];
            int l = i + 1, r = n - 1;
            if (nums[i] > 0) break;
            while (l < r)
            {
                int lNum = nums[l]; int rNum = nums[r];
                if (lNum + rNum == target)
                {
                    vector<int> temp {nums[i], lNum, rNum};
                    ans.push_back(temp);
                    // 判断左右窗口是否有重复数字，如果有跳过
                    while (l < r && nums[l] == lNum) ++l;
                    while (l < r && nums[r] == rNum) --r;
                }
                else if (lNum + rNum > target) --r;
                else ++l;
            }

            // 判断原始nums序列中，index下标是否有重复数字，如果有跳过
            while (i + 1 <= n - 3 && nums[i] == nums[i + 1]) ++i;
        }
        return ans;
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
            while (l < r && nums[r] > pivot) r--;
            nums[l] = nums[r];
            while (l < r && nums[l] < pivot) l++;
            nums[r] = nums[l];
            nums[l] = pivot;
        }
        return l;
    }
};