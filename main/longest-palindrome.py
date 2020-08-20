def findMaxPalindromeWindow(s: str, start: int, end: int) -> str:
    while start >= 0 and end < len(s) and s[start] == s[end]:
        start -= 1
        end += 1
    return s[start+1 : end]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        for index in range(0, len(s)):
            evenLenPalindrome = findMaxPalindromeWindow(s, index - 1, index)
            if len(evenLenPalindrome) > len(longest):
                longest = evenLenPalindrome
            oddLenPalindrome = findMaxPalindromeWindow(s, index - 1, index + 1)
            if len(oddLenPalindrome) > len(longest):
                longest = oddLenPalindrome
        return longest