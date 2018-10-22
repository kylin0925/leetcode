class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        #print(A,B)
        if A == B:
            return True
        for i in range(1,len(A)):
            tmp = A[i:] + A[0:i]
            if tmp == B:
                return True
        return False
sol = Solution()
test_data =[ ['abcde', 'cdeab'],["",""],["abc","abc"],["a","c"],["a"*99+"c","c"+"a"*99],["abc","ab"],["ab","eeeeee"]]
for d in test_data:
    print(sol.rotateString(d[0],d[1]))
