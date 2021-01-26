"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

但是会超时，虽然正确
"""
from typing import List, Mapping, NoReturn
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 堆排序
        # 大顶堆是顶为大数，越往下越小，小顶堆是顶为小数，越往下越大。因此此处使用K个元素的小顶堆，则顶为答案
        def build_heap(self, i: int, n: int) -> None:
            nums = self.nums
            # 左右子结点下标
            left = 2 * i + 1
            right = 2 * i + 2
            large_index = i

            if left <= n and nums[large_index] < nums[left]:
                large_index = left
            if right <= n and nums[large_index] < nums[right]:
                large_index = right
            if large_index != i:
                nums[i], nums[large_index] = nums[large_index], nums[i]
                self.build_heap(large_index, n)
            
        def heap_sort(self, nums):
            n = len(nums)

            # build a maxheap
            for i in range(n // 2 - 1, -1, -1):
                self.build_heap(i, n)
            
            for j in range(n - 1, -1, -1):
                nums[0], nums[j] = nums[j], nums[0]
                self.build_heap(0, j)
            
            return nums

        ans = []
        nums = self.nums
        for i in range(len(nums)):
            if i < k:
                ans.append(nums[i])
                heap_sort(ans)
            else:
                if ans[0] < nums[i]:
                    ans[0] = nums[i]
                    heap_sort(ans)
                else:
                    continue
        return ans[0]
