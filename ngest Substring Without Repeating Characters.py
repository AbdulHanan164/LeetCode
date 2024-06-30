class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        if (n == 0) return 0;
        
        vector<int> charMap(256, -1); // Map to store last seen index of each character
        int maxLength = 0;
        int start = 0;
        
        for (int i = 0; i < n; ++i) {
            if (charMap[s[i]] >= start) {
                start = charMap[s[i]] + 1; // Move start to avoid repeating character
            }
            charMap[s[i]] = i; // Update last seen index of character
            maxLength = max(maxLength, i - start + 1); // Update max length
        }
        
        return maxLength;
    }
};
