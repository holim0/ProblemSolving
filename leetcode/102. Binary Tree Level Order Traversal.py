# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer= {}

        level = 0

        def getSol(cur, level):
            if cur == None:
                return 

            if level not in answer:
                answer[level] = [cur.val]
            else:
                answer[level].append(cur.val)
            
            getSol(cur.left, level+1)
            getSol(cur.right, level+1)

        getSol(root, 0)
        order = []
        for key in answer:
            order.append(answer[key])
        
        return order