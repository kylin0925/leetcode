class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        res = []
        print nums
        for i in xrange(n):
            for j in xrange(i+1,n):
                ktmp = j+1;
                start = 0
                end = n
                
                if nums[i] + nums[j] > 0:
                    while ktmp < n and nums[ktmp] < 0:
                        ktmp +=1
                    #print ktmp    
                    start = 0
                    end = ktmp
                if nums[i] + nums[j] <= 0:    
                    while ktmp < n and nums[ktmp] < 0:
                        ktmp +=1
                    #print ktmp    
                    start = ktmp
                    end = n
                if start == i or start == j :
                    continue
                if end == i or end == j :    
                    continue
                if start == end :
                    continue
                if start <= j : 
                    continue
                #print start,end    
                for k in xrange(start,end):
                    #print i,j,k
                       
                    if nums[i] + nums[j] + nums[k] == 0:  
                        tmp = [nums[i] , nums[j] , nums[k]]
                        if res.count(tmp) == 0:
                            res.append(tmp)
                            
                            
                            
        return res
        

s = Solution()
print s.threeSum([-1,0,1,2,-1,-4])
#print s.threeSum([4,-2,-9,9,7,9,10,-15,4,-9,-9,8,-6,7,-7,-2,4,-9,-7,-11,13,9,5,-8,10,8,-6,-1,-2,-6,6,-12])