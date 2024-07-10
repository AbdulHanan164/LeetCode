class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        # Initialize result array with zeros
        res = [0] * (m + n)
        
        # Perform manual multiplication
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                product = digit1 * digit2
                pos1, pos2 = i + j, i + j + 1
                total = product + res[pos2]
                res[pos1] += total // 10
                res[pos2] = total % 10
        
        # Construct result string
        result = ''.join(map(str, res)).lstrip('0')
        
        return result if result else "0"
