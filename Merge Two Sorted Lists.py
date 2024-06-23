class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        # Dummy node initialization
        dummy = ListNode(-1)
        current = dummy
        
        # Pointers for both lists
        p1, p2 = l1, l2
        
        # Merge while both lists have nodes
        while p1 and p2:
            if p1.val <= p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
        
        # Append remaining nodes of l1 or l2 if any
        if p1:
            current.next = p1
        if p2:
            current.next = p2
        
        # Return the merged list starting from dummy.next
        return dummy.next
