""" 24. 两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
输入：head = [1,2,3,4]
输出：[2,1,4,3]
输入：head = []
输出：[]
输入：head = [1]
输出：[1]

时间： O(n), 空间: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    # 系统给出
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def swapPairs(self, head: ListNode) -> ListNode:
        # 建立伪节点
        dummy = ListNode(0)
        # 将链表与伪节点连接
        dummy.next = head
        cur = dummy
        # 当存在下一个和下下一个节点时
        while cur.next and cur.next.next:
            preNode, forNode = cur.next, cur.next.next
            # 开始反转preNode和forNode节点
            cur.next = forNode
            # 一定要先将反转后的前一个节点与反转前的forNode的下一个节点去关联，即连接到剩余还未反转的节点上
            preNode.next = forNode.next
            # 反转节点
            forNode.next = preNode
            # 更新cur节点位置
            cur = cur.next.next
        return dummy.next

