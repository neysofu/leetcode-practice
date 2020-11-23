class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = ''
        topDistance = max(2 * numRows - 2, 1)
        for i in range(0, numRows):
            if i == 0 or i == numRows - 1:
                step = topDistance
                while i < len(s):
                    zigzag += s[i]
                    i += topDistance
            else:
                step = topDistance - 2 * i
                while i < len(s):
                    zigzag += s[i]
                    i += step
                    step = topDistance - step
        return zigzag