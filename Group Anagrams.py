class Solution(object):
    def groupAnagrams(self, strs):
        from collections import defaultdict
        
        # Step 1: Initialize a hashmap to store grouped anagrams
        anagrams = defaultdict(list)
        
        # Step 2: Iterate through each string in strs
        for s in strs:
            # Sort the characters of the string to use as a key
            sorted_s = tuple(sorted(s))
            # Append the original string to the corresponding group in hashmap
            anagrams[sorted_s].append(s)
        
        # Step 3: Return the values of the hashmap as a list of lists
        return list(anagrams.values())
