"""
给定一个二叉树的根节点 root ，返回它的 中序 遍历。

输入：root = [1,null,2,3]
输出：[1,3,2]

输入：root = []
输出：[]
"""

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
