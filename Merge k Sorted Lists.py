import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        # Custom comparison function for ListNode objects
        def compare(node1, node2):
            return node1.val - node2.val
        
        # Initialize min-heap
        min_heap = []
        heapq.heapify(min_heap)
        
        # Push all heads of lists into the heap
        for head in lists:
            if head:
                heapq.heappush(min_heap, (head.val, head))
        
        # Dummy node for the result
        dummy = ListNode()
        current = dummy
        
        # Merge lists using the min-heap
        while min_heap:
            val, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, node.next))
        
        return dummy.next
