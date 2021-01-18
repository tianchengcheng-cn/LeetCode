"""
平衡二叉树
输入：root = [3,9,20,null,null,15,7]
输出：true

自顶向下：
O(n^2)， O(n)

自顶向下：
O(n)，空间复杂度取决于递归调用的层数
O(n)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        # 自顶向下
        def height(root):
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return 0
        return abs(height(root.left) - height(root.right)) <= 1 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)

        # 自底向顶
        def height(root):
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1
        return height(root) >= 0