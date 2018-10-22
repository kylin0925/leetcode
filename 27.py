class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cnt = 0
        nums_len = len(nums)
        for i in range(nums_len):
            #print "i",i
            if nums[i] == val:

                j = i +1
                while j<nums_len :
                    if nums[j]==nums[i]:
                        j+=1
                    else:
                        break
                #print j    
                if j < nums_len:
                    cnt+=1
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
                    #print "24",cnt,nums
            else:
                cnt+=1
                #print "else",cnt
        #print nums ,cnt       
        return cnt
sol = Solution()
test_data = [ [[3,2,2,3],3],[[1,2,3,4],0],[[1,2,3,4],4],[[0,1,2,2,3,0,4,2],2] ]
for d in test_data:
    print "res", sol.removeElement(d[0],d[1]),d[0]
