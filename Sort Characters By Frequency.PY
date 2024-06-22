class Solution(object):
    def frequencySort(self, s):
        from collections import Counter
        
        # Step 1: Count frequencies of each character
        frequency = Counter(s)
        
        # Step 2: Sort characters by frequency in descending order
        sorted_chars = sorted(frequency.items(), key=lambda x: -x[1])
        
        # Step 3: Construct the result string
        result = []
        for char, freq in sorted_chars:
            result.append(char * freq)
        
        return ''.join(result)
