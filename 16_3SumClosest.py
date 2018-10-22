class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums_len = len(nums)
        nums.sort()
        #print nums
        res = 0
        fst = 0
        sec = 1
        thrd = 2
       
        res = nums[fst] + nums[sec] + nums[thrd]
        
        while fst < nums_len-2:
           
            sec = fst +1
            thrd = nums_len -1
            #print fst,sec,thrd
            while sec < thrd :
                tmp = nums[fst] + nums[sec] + nums[thrd]
                
                #print "sec",sec,"thrd",thrd,tmp,abs(tmp-target)

                if abs(res-target) > abs(tmp-target):
                    res = tmp
                    #print "res",res
                if tmp > target:                        
                    thrd-=1
                else:                                        
                    sec+=1 
                        
            fst+=1            
        return res
        
test_data = [-3,0,1,2]
#test_data = [1,6,9,14,16,70]
#test_data = [1,2,4,8,16,32,64,128]
target = 1

sol = Solution()
print sol.threeSumClosest(test_data,target)