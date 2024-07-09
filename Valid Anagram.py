class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        # Use a dictionary to count character frequencies in s
        count_s = {}
        for char in s:
            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1
        
        # Compare character frequencies in t
        for char in t:
            if char in count_s:
                count_s[char] -= 1
                if count_s[char] < 0:
                    return False
            else:
                return False
        
        return True
