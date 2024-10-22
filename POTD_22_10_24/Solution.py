# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        if not root:
            
            return -1

        q=deque()

        q.append(root)

        r = []

        while q:

            n = len(q)

            cur_sum = 0

            for _ in range(n):

                node = q.popleft()

                if node.left:

                    q.append(node.left)

                if node.right:

                    q.append(node.right)

                cur_sum+=node.val

            r.append(cur_sum)

        if k<=len(r):

            return sorted(r)[-k]

        else:

            return -1


        