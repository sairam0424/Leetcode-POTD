# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:

            return 

        q = deque([root])

        r = []

        while q:

            cur_sum = 0

            for _ in range(len(q)):

                node = q.popleft()

                if node.left:

                    q.append(node.left)

                if node.right:

                    q.append(node.right)

                cur_sum+=node.val

            r.append(cur_sum)


        q.append(root)

        root.val = 0

        level_index = 1

        while q:

            for _ in range(len(q)):

                node = q.popleft()

                sibling_sum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)

                if node.left:

                    node.left.val =  r[level_index] - sibling_sum

                    q.append(node.left)

                if node.right:

                    node.right.val = r[level_index] - sibling_sum

                    q.append(node.right)


            level_index+=1

        return root

                



        


        