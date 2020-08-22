class Solution:
    def sortArrayByParity(self, A):
        pivot = 0
        i = 0
        while i < len(A):
            if A[i] % 2 == 0:
                A[i], A[pivot] = A[pivot], A[i]
                pivot += 1
            i += 1
        return A