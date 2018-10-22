class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
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
                return []
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

        res = []
        nums.sort()
        #print(nums)
        tmp = nums[:];
        res.append(tmp[:])
        while True:
            tmp = next_permutation(tmp)
            if tmp ==[]:
                break
            #print(tmp)
            res.append(tmp[:])

        return res
sol = Solution()

data = [ [1,3,2], [1]]
for d in data:
    print(sol.permuteUnique(d))
