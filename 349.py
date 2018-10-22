class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        
        return list(set1.intersection(set2))
sol = Solution()
test_data = [ [[],[]] , [[1,2,2,1],[2,2]], [[1,2,2,1],[]], [[1,2,2,1],[3,4]] ]
for d in test_data:
    print sol.intersection(d[0],d[1])
