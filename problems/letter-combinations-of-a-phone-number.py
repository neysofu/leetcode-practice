DIGITS_TO_LETTERS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        combinations = ['']
        for digit in digits:
            combinations = [combo + letter for letter in DIGITS_TO_LETTERS[digit] for combo in combinations]
        return combinations