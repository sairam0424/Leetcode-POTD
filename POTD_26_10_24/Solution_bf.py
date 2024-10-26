# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        heights_after_removal = [0]*(100001)

        self.max_height = 0

        def dfs_lefttoright(root,cur_height):

            if not root:

                return 

            heights_after_removal[root.val] = self.max_height

            self.max_height = max(self.max_height,cur_height)

            dfs_lefttoright(root.left,cur_height+1)

            dfs_lefttoright(root.right,cur_height+1)


        def dfs_righttoleft(root,cur_height):

            if not root:

                return 

            heights_after_removal[root.val] = max(heights_after_removal[root.val],self.max_height)

            self.max_height = max(self.max_height,cur_height)

            dfs_righttoleft(root.right,cur_height+1)

            dfs_righttoleft(root.left,cur_height+1)

        
        dfs_lefttoright(root,0)

        self.max_height = 0

        dfs_righttoleft(root,0)

        return [heights_after_removal[query] for query in queries]

        

        


        



        

    
        