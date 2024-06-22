class Solution(object):
    def minWindow(self, s, t):
        from collections import defaultdict
        
        if not s or not t:
            return ""
        
        required = defaultdict(int)
        for char in t:
            required[char] += 1
        
        left, right = 0, 0
        formed = 0
        window = defaultdict(int)
        
        min_length = float('inf')
        start_index = 0
        
        while right < len(s):
            char = s[right]
            window[char] += 1
            
            if char in required and window[char] == required[char]:
                formed += 1
            
            while formed == len(required) and left <= right:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    start_index = left
                
                char = s[left]
                window[char] -= 1
                if char in required and window[char] < required[char]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        if min_length == float('inf'):
            return ""
        else:
            return s[start_index:start_index + min_length]
