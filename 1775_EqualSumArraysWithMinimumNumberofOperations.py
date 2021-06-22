from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort(reverse=True)
        nums2.sort(reverse=True)
        nums1_sum = sum(nums1)
        nums2_sum = sum(nums2)
        print(nums1,nums2)
        def solv(small,small_sum,large,large_sum):
            if len(small)*6 <len(large):
                return -1

            sum_diff = large_sum - small_sum
            #print(sum_diff)
            si = li = 0
            qs = [6-x for x in small]
            ql =[x-1 for x in large]
            qall = qs+ql
            qall.sort(reverse=True)
            while sum_diff > 0:
                sum_diff -=qall[si]
                si+=1
                #print(sum_diff)
            return si

        if sum(nums1) > sum(nums2):
            return solv(nums2,nums2_sum,nums1,nums1_sum)
        else:
            return solv(nums1,nums1_sum,nums2,nums2_sum)

#print(Solution().minOperations(nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]))
#print(Solution().minOperations(nums1 = [1,1,1,1,1,1,1], nums2 = [6]))

import random
nums = []
for c in range(2):
    a = random.randint(1,10**5)
    #print(a)
    for i in range(a):
        nums.append(random.randint(1,6))
    print(nums)
    nums=[]