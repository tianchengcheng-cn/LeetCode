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
        """ -----> O(nlogn),  O(logn)
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
        """

        """-----> O(nlogn), O(1)
        迭代的化，空间复杂度就会是 O(1)
        """
        def split(head, step):
            if not head: return

            cur = head
            while step and cur.next:
                cur = cur.next
                step -= 1
            right = cur.next
            cur.next = None
            return right

        def merge(left, right):
            dummy = ListNode(0)
            cur = dummy
            while left and right:
                if left.val < right.val: cur.next, left = left, left.next
                else: cur.next, right = right, right.next
                cur = cur.next
            cur.next = left if left else right
            return dummy.next
        
        def getLength(head):
            length = 1
            cur = head
            while cur:
                cur = cur.next
                length += 1
            return length

        length = getLength(head)
        step = 1
        
        while (step < length):
            dummy = ListNode(0)
            dummy.next = head
            slow, fast = dummy, dummy.next
            while (fast):
                head1 = fast
                head2 = split(head=head1, step=step)
                temp = merge(head1, head2)
                fast = split(head=head2, step=step)
                slow.next = temp
                while (slow.next):
                    slow = slow.next
            step *= 2
        return dummy.next
        


            