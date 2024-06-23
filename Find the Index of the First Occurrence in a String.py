class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        
        # Step 1: Build the LPS (Longest Prefix which is also Suffix) array for needle
        lps = [0] * len(needle)
        j = 0  # length of the previous longest prefix suffix
        i = 1
        
        while i < len(needle):
            if needle[i] == needle[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    lps[i] = 0
                    i += 1
        
        # Step 2: Search for needle in haystack using the LPS array
        i = 0  # index for haystack
        j = 0  # index for needle
        
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            
            if j == len(needle):
                return i - j
            
            elif i < len(haystack) and haystack[i] != needle[j]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        
        return -1
