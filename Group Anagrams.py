class Solution:
    def groupAnagrams(self, strs):
        anagrams_map = {}
        
        for s in strs:
            sorted_tuple = tuple(sorted(s))
            if sorted_tuple in anagrams_map:
                anagrams_map[sorted_tuple].append(s)
            else:
                anagrams_map[sorted_tuple] = [s]
        
        return list(anagrams_map.values())
