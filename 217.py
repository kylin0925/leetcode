class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        t = {}
        for i in nums:
            if t.has_key(i) == False:
                t[i] = 1
            else:
                return True
        return False        
sol = Solution()
test_data = [[1,2,3,1],[1,2,3,4],[1,1,1,3,3,4,3,2,4,2] ]
for d in test_data:
    print sol.containsDuplicate(d)
