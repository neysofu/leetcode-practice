class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ''
        prefix = strs[0]
        for string in strs:
            if len(string) < len(prefix):
                prefix = prefix[:len(string)]
            for (i, c) in enumerate(prefix):
                if c != string[i]:
                    prefix = prefix[:i]
                    break
        return prefix