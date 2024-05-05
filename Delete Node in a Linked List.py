class Solution:
    def deleteNode(self, node):
        # Copy the value of the next node to the current node
        node.val = node.next.val
        # Delete the next node
        node.next = node.next.next
