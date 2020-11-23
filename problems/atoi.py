DIGITS = '0123456789'

class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip(' ')
        if len(str) == 0:
            return 0
        if str[0] == '+':
            sign = 1
            i = 1
        elif str[0] == '-':
            sign = -1
            i = 1
        elif str[0] in DIGITS:
            sign = 1
            i = 0
        else:
            return 0
        result = 0
        for c in str[i:]:
            if c not in DIGITS:
                break
            result *= 10
            result += int(c)
        return max(min(result * sign, 2**31 - 1), -2**31)
