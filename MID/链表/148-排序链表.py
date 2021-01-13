"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
输入：head = [4,2,1,3]
输出：[1,2,3,4]
输入：head = []
输出：[]
"""

"""
O(nlogn)时间复杂度，需要用到二分法
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        slow, fast = head, head.next

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        mid, slow.next = slow.next, None

        left, right = self.sortList(head), self.sortList(mid)

        # 归并排序
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val: h.next, left = left, left.next
            else: h.next, right = right, right.next
            h = h.next
        h.next = left if left else right

        return res.next