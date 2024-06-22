class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positives = []
        negatives = []
        
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)
        
        result = []
        i, j = 0, 0
        while i < len(positives) and j < len(negatives):
            result.append(positives[i])
            result.append(negatives[j])
            i += 1
            j += 1
        
        return result
