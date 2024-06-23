class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Handle zero dividend case
        if dividend == 0:
            return 0
        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        # Determine sign of the result
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Convert to absolute values
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        # Loop until dividend is greater than or equal to divisor
        while dividend >= divisor:
            # Calculate how many times the divisor can be subtracted from the dividend
            temp_divisor = divisor
            temp_quotient = 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                temp_quotient <<= 1
            
            # Subtract the shifted divisor from the dividend
            dividend -= temp_divisor
            # Add the quotient count from this iteration
            quotient += temp_quotient
        
        # Handle the sign of the quotient
        if negative:
            quotient = -quotient
        
        # Ensure the result is within the 32-bit signed integer range
        if quotient < INT_MIN:
            return INT_MIN
        elif quotient > INT_MAX:
            return INT_MAX
        else:
            return quotient
