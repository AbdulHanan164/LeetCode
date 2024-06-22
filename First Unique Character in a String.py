class Solution(object):
    def firstUniqChar(self, s):
        from collections import Counter
        
        # Step 1: Use Counter to count frequencies of each character
        count = Counter(s)
        
        # Step 2: Find the index of the first non-repeating character
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        
        # Step 3: If no non-repeating character found, return -1
        return -1
