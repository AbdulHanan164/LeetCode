class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        # Calculate the height of the tree
        def height(node):
            h = 0
            while node.left:
                node = node.left
                h += 1
            return h
        
        h = height(root)
        
        if h == 0:
            return 1  # Only the root node exists
        
        # Function to check if a node exists at index idx in the last level
        def exists(idx):
            bits = 1 << (h - 1)
            node = root
            while node and bits > 0:
                if bits & idx == 0:
                    node = node.left
                else:
                    node = node.right
                bits >>= 1
            return node is not None
        
        # Binary search to find the last existing node
        left, right = 0, (1 << h) - 1
        while left <= right:
            mid = (left + right) // 2
            if exists(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        # Number of nodes in the tree
        return (1 << h) - 1 + left
