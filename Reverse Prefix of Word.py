class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Find the index of the first occurrence of character ch
        index = word.find(ch)

        # If ch is not found, return the original word
        if index == -1:
            return word

        # Reverse the substring of word from index 0 to the index of ch
        return word[:index + 1][::-1] + word[index + 1:]
