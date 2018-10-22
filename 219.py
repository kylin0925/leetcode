class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_len = len(nums)
        i = 0
        t = {}
        while i < nums_len:
            if t.has_key(nums[i]) == False:
                t[nums[i]] = i
            else:
                l = t[nums[i]]
                if i-l <=k:
                    return True
                else:
                    t.pop(nums[i])
                    t[nums[i]] = i
            i+=1
        return False
sol = Solution()
test_data = [ [[1,2,3,1], 3], [[1,0,1,1],1], [[1,2,1], 0],[[1,2,3,4,1],3],[[1,2,3,4,1],4] ]
for d in test_data:
    print sol.containsNearbyDuplicate(d[0],d[1])
