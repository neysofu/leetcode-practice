SYMBOLS = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        last_value = 0
        for c in s:
            new_value = SYMBOLS[c]
            if last_value < new_value:
                result -= last_value * 2
            result += new_value
            last_value = new_value
        return result