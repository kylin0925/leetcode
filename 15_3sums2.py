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
        
        i = 0
        while i < n-2:
            target = -nums[i]
            start = i + 1
            end = n-1
            #print i,start,end
            while start < end :
                tmp = nums[start] + nums [end]
                #print start,end," tmp ",tmp
                if tmp > target:
                    end-=1
                elif tmp < target:
                    start +=1
                else:
                    tmp = [nums[i] , nums[start] , nums[end]]              
                    res.append(tmp)
                    while start<end and nums[start]== nums[start+1]:
                        start+=1
                    while end>start and nums[end]== nums[start-1]:
                        end-=1    
                    start+=1
            
            while i<n-1 and nums[i]== nums[i+1]:
                i +=1
            i+=1    
        return res
        

s = Solution()
print s.threeSum([-1,0,1,2,-1,-4])
print s.threeSum([0,0,0,0])
print s.threeSum([0,0,0])
print s.threeSum([1,0,-1,-1])
print s.threeSum([4,-2,-9,9,7,9,10,-15,4,-9,-9,8,-6,7,-7,-2,4,-9,-7,-11,13,9,5,-8,10,8,-6,-1,-2,-6,6,-12])