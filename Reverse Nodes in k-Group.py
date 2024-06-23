class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        # Helper function to reverse a sublist of size k
        def reverse_sublist(head, k):
            prev = None
            curr = head
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        # Create a dummy node to simplify handling edge cases
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        
        while True:
            # Check if there are k nodes remaining
            check_node = prev
            for _ in range(k):
                if not check_node.next:
                    return dummy.next
                check_node = check_node.next
            
            # Initialize curr and next_start for the sublist to be reversed
            curr = prev.next
            next_start = curr
            
            # Move curr k steps forward
            for _ in range(k):
                next_start = next_start.next
            
            # Reverse the sublist from curr to next_start
            new_head = reverse_sublist(curr, k)
            
            # Connect the reversed sublist back into the main list
            prev.next = new_head
            curr.next = next_start
            
            # Update prev and continue to the next sublist
            prev = curr
