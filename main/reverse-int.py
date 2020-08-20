import math

class Solution:
    def reverse(self, x: int) -> int:
        isNegative = x < 0
        x = abs(x)
        numDigits = math.ceil(math.log10(x))
        result = 0
        for i in range(numDigits):
            digit = 
            result += x // 10 + (x % 10) * 10**(numDigits - d + 1)
        if isNegative:
            return -result
        return result