class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        maxlen = 0
        alen = len(A)
        A.sort(reverse=True)
        for i in range(alen):
            for j in range(i+1,alen):
                for k in range(j+1,alen):
                    if A[i] + A[j] > A[k] and A[j] + A[k] > A[i] and A[i] + A[k] > A[j]:
                        return A[i] + A[j] + A[k]
                    if A[i] + A[j] > A[k]:
                        break
        return maxlen