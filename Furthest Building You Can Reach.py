import heapq

class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        n = len(heights)
        min_heap = []
        
        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            
            if diff <= 0:
                continue
            
            heapq.heappush(min_heap, diff)
            
            if len(min_heap) > ladders:
                bricks -= heapq.heappop(min_heap)
            
            if bricks < 0:
                return i
        
        return n - 1
