"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
时间：O(n), 空间：O(1)
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 构建伪节点
        dummy = ListNode(0)
        # 检索节点
        cur = dummy
        # 如果l1和l2均有节点，判断节点值，更新伪节点链表
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        # 连接剩余节点
        cur.next = l1 if l1 else l2
        return dummy.next