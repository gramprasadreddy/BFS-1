# Binary Tree Level Order Traversal (https://leetcode.com/problems/binary-tree-level-order-traversal/)

# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on GFG : YES
# Any problem you faced while coding this : NO


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []
        
        q = deque()
        q.append(root) # put root in queue
        res = []
        currlevel = 0

        while q: # while q is not empty
            len_q = len(q)
            res.append([]) # append an empty list

            for _ in range(len_q): # loop until the length of the q from previous step

                node = q.popleft() # pop front
                res[currlevel].append(node.val) # at the currlevel append the value of the root

                if node.left is not None: # go left and put left in q
                    q.append(node.left)
                
                if node.right is not None: # same thing for right
                    q.append(node.right)
            
            currlevel +=1 # increase currlevel when we put children
        
        return res

        