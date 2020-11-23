import math

SYMBOLS_FOR_1 = ['I', 'X', 'C', 'M']
SYMBOLS_FOR_5 = ['V', 'L', 'D']

class Solution:
    def intToRoman(self, num: int) -> str:
        num_digits = math.floor(math.log10(num)) + 1
        roman = ''
        for i in range(num_digits):
            i = num_digits - i - 1
            # Iterate over digits from most to least significant.
            digit = (num // 10**i) % 10
            if digit <= 3:
                roman += SYMBOLS_FOR_1[i] * digit
            elif digit == 4:
                roman += SYMBOLS_FOR_1[i] + SYMBOLS_FOR_5[i]
            elif digit == 5:
                roman += SYMBOLS_FOR_5[i]
            elif digit <= 8:
                roman += SYMBOLS_FOR_5[i] + SYMBOLS_FOR_1[i] * (digit - 5)
            else:
                roman += SYMBOLS_FOR_1[i] + SYMBOLS_FOR_1[i+1]
        return roman