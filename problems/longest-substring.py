class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = longest = 0
        start = end = 0
        letters = set({})
        while end < len(s):
            if s[end] in letters:
                letters.remove(s[start])
                start += 1
                length -= 1
            else:
                letters.add(s[end])
                end += 1
                length += 1
                if length > longest:
                    longest += 1
        return longest