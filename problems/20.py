class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = []
        for i in range(len(s)):
            if s[i] in "([{":
                parentheses.append(i)
            elif len(parentheses) == 0:
                return False
            else:
                j = parentheses.pop()
                if not ((s[i] == ')' and s[j] == '(')
                     or (s[i] == ']' and s[j] == '[')
                     or (s[i] == '}' and s[j] == '{')):
                    return False
        return len(parentheses) == 0
