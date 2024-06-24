class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        current = root
        
        while current or stack:
            # Traverse leftmost nodes and push onto stack
            while current:
                stack.append(current)
                current = current.left
            
            # Pop the node from stack, visit it, then move to its right subtree
            current = stack.pop()
            result.append(current.val)
            current = current.right
        
        return result
