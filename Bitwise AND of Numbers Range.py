class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        while left < right:
            right &= (right - 1)  # Clear the least significant set bit of right
        return right
