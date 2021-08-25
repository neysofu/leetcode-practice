class Solution:
    def isMatch(self, s: str, pattern: str) -> bool:
        states = [(0, 0)]
        while len(states) > 0:
            new_states = set()
            for (i, j) in states:
                if i == len(s) and j == len(pattern):
                    return True
                elif j == len(pattern):
                    continue
                has_kleene_star = (j+1) < len(pattern) and pattern[j+1] == '*'
                match = lambda c: c == '.' or s[i] == c
                if has_kleene_star:
                    # You can always skip the Kleene star!
                    new_states.add((i, j+2))
                if i < len(s) and match(pattern[j]):
                    j_offset = 0 if has_kleene_star else 1
                    new_states.add((i+1, j+j_offset))
            states = new_states
        return False