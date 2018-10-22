class Solution(object):
    def twosum(self,nums,left,right,target):
        #print target
        res = []
        while left < right:
            #print left,right,nums[left] + nums[right]
            if nums[left] + nums[right] > target:
                right -=1
            elif nums[left] + nums[right] < target:
                left +=1
            else:
                res.append( [nums[left],nums[right]])
                while nums[right] == nums[right -1]:
                    right-=1
                right-=1    
        #print "res",res        
        return res
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) == 4:
            if nums[0] + nums[1] + nums[2] + nums[3] == target:
                return [[nums[0] , nums[1] , nums[2] , nums[3]]]
            else:
                return []
        res = []
        nums.sort()
        #print nums
        i = j =k = l = 0
        nums_len = len(nums)
        while i < nums_len - 3:
            #print "i",i
            j = i+1
            while j < nums_len -2:
                #print "j",j
                tmp = nums[i] + nums[j]
                tmp = target - tmp
                towsumlist = self.twosum(nums,j+1,len(nums)-1,tmp)
                if towsumlist!=[]:
                    for row in towsumlist:
                        #print nums[i],nums[j],row[0],row[1]
                        res.append([nums[i],nums[j],row[0],row[1]])
                #j+=1
                tmp = j            
                while tmp < nums_len-1 and nums[tmp+1] == nums[j]: 
                    j+=1
                    tmp=j
                    #print j
                j+=1
            tmp = i
            while tmp < nums_len-1 and nums[tmp+1] == nums[i]: 
                i+=1
                tmp=i
                #print i
            i+=1    
        return res
sol = Solution()
test_data = [ [[5,5,3,5,1,-5,1,-2],4], [[1, 0, -1, 0, -2, 2],3],[[-3,-2,-1,0,0,1,2,3],0],]
for d in test_data:
    print d[0],d[1]
    print sol.fourSum(d[0],d[1])