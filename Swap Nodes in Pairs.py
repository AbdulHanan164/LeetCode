class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        # Create a dummy node to simplify handling edge cases
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            # Nodes to be swapped
            current = prev.next
            next = current.next
            
            # Swapping
            prev.next = next
            current.next = next.next
            next.next = current
            
            # Move to the next pair
            prev = current
        
        return dummy.next
