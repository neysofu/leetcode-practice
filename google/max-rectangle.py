def findLargestRectFromPoint(matrix, x, y):
    area = 1


class Solution:
    def maximalRectangle(self, matrix) -> int:
        for (y, row) in enumerate(matrix):
            for (x, value) in enumerate(row):
                if value == '1':
                    findLargestRectFromPoint(matrix, x, y)