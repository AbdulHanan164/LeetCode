from collections import defaultdict

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_length = len(words[0])
        total_length = len(words) * word_length
        result = []
        
        # Create a frequency dictionary for words
        expected_counts = defaultdict(int)
        for word in words:
            expected_counts[word] += 1
        
        for i in range(len(s) - total_length + 1):
            actual_counts = defaultdict(int)
            found = True
            for j in range(i, i + total_length, word_length):
                word = s[j:j + word_length]
                if word in expected_counts:
                    actual_counts[word] += 1
                    if actual_counts[word] > expected_counts[word]:
                        found = False
                        break
                else:
                    found = False
                    break
            if found:
                result.append(i)
        
        return result
