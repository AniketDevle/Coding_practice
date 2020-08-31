"""

Breadth First search 
"""

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        queue = collections.deque([(root)])
        
        while queue:
            
            node = queue.popleft()
            if node:
                node.left , node.right = node.right , node.left
                queue.append(node.left)
                queue.append(node.right)
        
        return root
        

"""

Depth First Search

"""
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        Stack = [root]
        
        while Stack:
            
            node = Stack.pop()
            if node:
                node.left , node.right = node.right , node.left 
                
                Stack.extend([node.right , node.left])
        
        
        return root        
