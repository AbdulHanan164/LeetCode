class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        s_to_t = {}
        t_to_s = {}
        
        for s_char, t_char in zip(s, t):
            if s_char in s_to_t:
                if s_to_t[s_char] != t_char:
                    return False
            elif t_char in t_to_s:
                if t_to_s[t_char] != s_char:
                    return False
            else:
                s_to_t[s_char] = t_char
                t_to_s[t_char] = s_char
        
        return True
