class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def next_permutation(lex):
            lex_len = len(lex)
            i = lex_len - 1
            # print i
            while i > 0:
                if lex[i] <= lex[i - 1]:
                    i -= 1
                else:
                    break

            if i == 0:
                return lex.sort()
            p = lex[i - 1]
            j = lex_len - 1
            while lex[j] <= p:
                j -= 1

            #print p, i, j, lex
            tmp = lex[i - 1]
            lex[i - 1] = lex[j]
            lex[j] = tmp
            # print p,tmp,i,j,lex

            # reverse
            res = lex[:i - 1:-1]
            head = lex[0:i]
            tmp = head + res
            for i in range(len(tmp)):
                lex[i] = tmp[i]
            return lex
        nums = next_permutation(nums)
        #print("tmp ",tmp)
        #nums = tmp.copy()
        #print("nums",nums)
sol = Solution()

data = [ [1,3,2],[1,1,5], [2,1,3],[1] ]
for d in data:
    sol.nextPermutation(d)
    print("ans ",d)