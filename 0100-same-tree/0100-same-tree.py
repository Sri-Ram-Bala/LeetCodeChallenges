# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def level_order_traversal(self, root):
        value = []
        if not root:
            return
        queue = deque([root])
        while queue:
            try:
                node = queue.popleft()
                value.append(node.val if node else None)
                queue.append(node.left)
                queue.append(node.right)
            except AttributeError:
                pass
        return value

    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        p_vals = self.level_order_traversal(p)
        q_vals = self.level_order_traversal(q)
        print(p_vals, q_vals)
        if p_vals == q_vals:
            return True
        return False


