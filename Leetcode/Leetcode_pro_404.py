# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        Stack = [root]
        ans = 0
        
        while (Stack):
            
            Node = Stack.pop()
            if Node:
                if Node.left and not Node.left.left and not Node.left.right:
                    ans = ans + Node.left.val
                if Node.left == None and Node.right:
                    Stack.extend([Node.right])
                elif Node.right == None and Node.left:
                    Stack.extend([Node.left])
                elif Node.left and Node.right:
                    Stack.extend([Node.left,Node.right])
                    
        return ans
        
        
