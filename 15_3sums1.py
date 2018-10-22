class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        res = []
        #print nums
        
        ii =-1
        for i in xrange(n-1):
            if ii != -1 and nums[i] == nums[ii]:
                continue
            #print ii,i  
            second = -1    
            for j in xrange(i+1,n):
                if second !=-1 and nums[second] == nums[j]:
                    continue
                target = -(nums[i] + nums[j])
                
                start = j +1
                end = n-1
                
                #print "==> ",target,nums[i],nums[j],start,end
                found = False
                while start <= end:
                    idx = (start + end ) /2
                    #print "bin ",start,end
                    if nums[idx] == target:
                        #print "found ",idx
                        found = True
                        break
                    else:
                        if nums[idx] > target:
                            end = idx -1
                        else:
                            start = idx +1
                            
                #print idx         
                if found == True:    
                    tmp = [nums[i] , nums[j] , nums[idx]]              
                    res.append(tmp)
                    #print res            
                second = j            
            ii = i                
        return res
        

s = Solution()
print s.threeSum([-1,0,1,2,-1,-4])
print s.threeSum([0,0,0,0])
print s.threeSum([0,0,0])
print s.threeSum([1,0,-1,-1])
#print s.threeSum([4,-2,-9,9,7,9,10,-15,4,-9,-9,8,-6,7,-7,-2,4,-9,-7,-11,13,9,5,-8,10,8,-6,-1,-2,-6,6,-12])