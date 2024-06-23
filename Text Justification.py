class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        current_line = []
        current_length = 0
        i = 0
        
        while i < len(words):
            # Check if we can add the next word in current line
            if current_length + len(words[i]) + len(current_line) <= maxWidth:
                current_line.append(words[i])
                current_length += len(words[i])
                i += 1
            else:
                # Distribute spaces for the current line
                num_words = len(current_line)
                if num_words == 1 or i == len(words):  # Left justify for single word or last line
                    result.append(' '.join(current_line).ljust(maxWidth))
                else:
                    total_spaces = maxWidth - current_length
                    num_gaps = num_words - 1
                    if num_gaps > 0:
                        min_spaces_per_gap = total_spaces // num_gaps
                        extra_spaces = total_spaces % num_gaps
                        
                        line = ''
                        for j in range(num_words - 1):
                            line += current_line[j]
                            line += ' ' * min_spaces_per_gap
                            if extra_spaces > 0:
                                line += ' '
                                extra_spaces -= 1
                                
                        line += current_line[-1]  # Add the last word without trailing spaces
                        result.append(line)
                    else:
                        result.append(current_line[0].ljust(maxWidth))
                
                # Reset for the next line
                current_line = []
                current_length = 0
        
        # Last line special case (left justified)
        last_line = ' '.join(current_line)
        last_line = last_line.ljust(maxWidth)
        result.append(last_line)
        
        return result
