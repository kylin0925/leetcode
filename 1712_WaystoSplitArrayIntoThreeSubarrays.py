from typing import List

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        numlen = len(nums)
        prefix = [ 0 for i in range(numlen)]
        prefix[0] = nums[0]
        for i in range(1,numlen):
            prefix[i] =  nums[i]+prefix[i-1]
        #print(prefix)
        ans = 0
        # i mid start
        # j r start

        for i in range(1,numlen):
            if prefix[i-1] > prefix[numlen-1] -prefix[i-1]:
                break
            for j in range(i+1,numlen):
                left = prefix[i-1]
                mid = prefix[j-1]-left
                r = prefix[numlen-1] - prefix[j-1]
                #print(left,mid,r)
                if left < mid < r:
                    ans+=1

                if mid > r:
                    break
        return ans

print("start")
#print(Solution().waysToSplit( nums =[1,2,2,2,5,0])  )
print(Solution().waysToSplit( nums =[x for x in range(10**5)])  )
print("end")