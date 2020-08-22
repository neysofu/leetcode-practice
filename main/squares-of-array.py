class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if len(A) == 0:
            return result
        pivot = 0
        while pivot < len(A) and A[pivot] < 0:
            pivot += 1
        l = pivot - 1
        r = pivot
        result = []
        while r < len(A) and l >= 0:
            a = A[r]
            b = -A[l]
            if a < b:
                result.append(a**2)
                r += 1
            else:
                result.append(b**2)
                l -= 1
        while r < len(A):
            result.append(A[r]**2)
            r += 1
        while l >= 0:
            result.append(A[l]**2)
            l -= 1
        return result