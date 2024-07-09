class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        unordered_map<char, char> s_to_t;
        unordered_map<char, char> t_to_s;
        
        for (int i = 0; i < s.length(); ++i) {
            char char_s = s[i];
            char char_t = t[i];
            
            if (s_to_t.find(char_s) == s_to_t.end() && t_to_s.find(char_t) == t_to_s.end()) {
                // If neither mapping exists, create mappings
                s_to_t[char_s] = char_t;
                t_to_s[char_t] = char_s;
            } else if (s_to_t[char_s] != char_t || t_to_s[char_t] != char_s) {
                // If mappings exist but are incorrect, return false
                return false;
            }
        }
        
        return true;
    }
};
