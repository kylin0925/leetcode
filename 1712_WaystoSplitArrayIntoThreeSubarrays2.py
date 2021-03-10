from typing import List

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        print(nums)
        def search_max(l,r,prefix):
            left = prefix[l-1]
            mi = -1
            #print("l",l,"r",r)
            while l+1<r:
                mi = (l+r)//2
                right = prefix[-1] - prefix[mi]
                mid = prefix[mi] - left
                #print(left,mid,right)
                if mid > right:
                    r = mi
                else:
                    l = mi
            #print(l,mi,r)
            #print("final r",left, prefix[r] -left, prefix[len(prefix)-1] - prefix[r])
            #print("final l",left, prefix[l] -left, prefix[len(prefix)-1] - prefix[l])
            if left <= prefix[r] -left <= prefix[len(prefix)-1] - prefix[r]:
                return r
            if left <= prefix[l] -left <= prefix[len(prefix)-1] - prefix[l]:
                return l
            return -1
        def search_min(l,r,prefix):
            left = prefix[l - 1]
            mi = -1
            # print("l",l,"r",r)
            while l + 1 < r:
                mi = (l + r) // 2
                right = prefix[-1] - prefix[mi]
                mid = prefix[mi] - left
                #print(left, mid, right)
                if left <= mid <= right:
                    r = mi
                else:
                    l = mi
            # print(l,mi,r)
            # print("final r",left, prefix[r] -left, prefix[len(prefix)-1] - prefix[r])
            # print("final l",left, prefix[l] -left, prefix[len(prefix)-1] - prefix[l])
            if left <= prefix[l] - left <= prefix[len(prefix) - 1] - prefix[l]:
                return l
            if left <= prefix[r] - left <= prefix[len(prefix) - 1] - prefix[r]:
                return r

            return -1
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
            #if prefix[i-1] > prefix[numlen-1] - prefix[i-1]:
            #    break
            mr = search_max(i,numlen-2,prefix)
            #print("find max",i,mr)
            if mr ==-1:
                continue
            ml = search_min(i,mr,prefix)
            #print(mr,ml,mr-ml+1)
            ans+=mr-ml+1
        return ans % (10**9 + 7)

print("start 2")
#print(Solution().waysToSplit( nums =[1,2,2,2,5,0])  )
print("ans",Solution().waysToSplit( nums =[1,1,1,1,1,1,10])  )
print("ans",Solution().waysToSplit( nums =[1,1,1,1,1,10])  )
print("ans",Solution().waysToSplit( nums =[x%10000 for x in range(10**5)])  )
print("end")