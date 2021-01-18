# from typing import TreeNode

"""
参考题解：Orust
时间：O(logN * logN) -> 最后一层mid，二分；根节点到最后一层path，二分；
空间：O(1)
"""


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        """ # 暴力递归
        if not root:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1 """

        """ # 二分查找，深度 + 递归
        if not root: return 0
        
        def left_height(node):
            return left_height(node.left) + 1 if node else 0

        def right_height(node):
            return right_height(node.right) + 1 if node else 0

        l = left_height(root.left)
        r = right_height(root.right)

        if l == r:
            return pow(2, l) - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1 """

        def path(root, num):
            for s in bin(num)[3:]:
                if s == '0':
                    root = root.left
                else:
                    root = root.right
                if not root: return False
            return True


        depth = 0
        cur = root
        while cur.left:
            depth += 1
            cur = cur.left
        
        left = 2 ** depth
        right = 2 ** (depth + 1) - 1

        while left < right:
            mid = (left + right + 1) // 2
            if path(root, mid):
                left = mid
            else:
                right = mid - 1
        return left
