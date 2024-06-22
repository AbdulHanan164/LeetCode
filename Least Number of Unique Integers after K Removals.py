class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        
        # Step 1: Count frequencies of each element
        freq = Counter(arr)
        
        # Step 2: Sort by frequency, then by element value
        sorted_freq = sorted(freq.items(), key=lambda x: (x[1], x[0]))
        
        # Step 3: Remove elements with the lowest frequencies until k elements are removed
        num_unique = len(freq)
        for value, count in sorted_freq:
            if k >= count:
                k -= count
                num_unique -= 1
            else:
                break
        
        # Step 4: Return the number of unique elements left
        return num_unique
