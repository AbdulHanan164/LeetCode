from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i, char in enumerate(strs[0]):
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    return strs[0][:i]  # Return the prefix found so far
        return strs[0]
