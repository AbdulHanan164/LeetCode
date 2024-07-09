class Solution(object):
    def removeElements(self, head, val):
        # Handle edge case of empty list
        while head and head.val == val:
            head = head.next
        
        if not head:
            return None
        
        prev = head
        curr = head.next
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return head
