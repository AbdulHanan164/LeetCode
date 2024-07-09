class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        # Step 1: Find the middle of the linked list using slow and fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # At this point, slow is at the middle of the linked list
        # If the length of the list is odd, move slow one step further
        if fast:
            slow = slow.next
        
        # Step 2: Reverse the second half of the linked list
        second_half = self.reverseList(slow)
        
        # Step 3: Compare the first half with the reversed second half
        first_half = head
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        return True
    
    def reverseList(self, head):
        """
        Helper function to reverse a linked list.
        """
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
