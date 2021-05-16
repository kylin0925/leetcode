from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        import math
        l = 1
        r = max(nums)
        while l < r:
            m = (l + r) >> 1
            #print(l,r,m)
            s = 0
            for e in nums:
                s += math.ceil(e/m)-1

            #print("sum op",s)
            if s > maxOperations:
                l = m+1
            else:
                r = m
        return l
#print(Solution().minimumSize(nums = [2,4,8,2], maxOperations = 4))
#print(Solution().minimumSize(nums = [2,2,2,2,2,2], maxOperations = 4))
print(Solution().minimumSize(nums = [7,17], maxOperations = 2))

import random
MAXLEN = 10
MAXOP =  10
def genTest():
    arr = [random.randint(1,MAXOP) for i in range(1,random.randint(1,MAXLEN))]
    op = random.randint(1,MAXOP)
    return arr,op
a,b =genTest()
print(a)
print(b)
