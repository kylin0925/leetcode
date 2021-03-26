from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hashtbl = {}
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                tmp = nums[i]*nums[j]
                hashtbl[tmp] = hashtbl.get(tmp,0)+1
                #print(nums[i],nums[j],nums[i]*nums[j])
        ans=0
        # c n 2 = n
        for k in hashtbl.keys():
            ans+=(hashtbl[k]*(hashtbl[k]-1))//2*8

        return ans


print(Solution().tupleSameProduct([2,3,4,6]))
print(Solution().tupleSameProduct([1,2,4,5,10]))
print(Solution().tupleSameProduct(nums = [2,3,4,6,8,12]))
print(Solution().tupleSameProduct(nums = [2,3,5,7]))