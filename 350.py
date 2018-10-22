class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        n1_len = len(nums1)
        n2_len = len(nums2)
        res = []
        n = min(n1_len,n2_len)
        i=0
        j=0
        while i < n1_len and j < n2_len :
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i+=1
                j+=1
            else:
                if nums1[i] < nums2[j]:
                    i+=1
                else:
                    j+=1
        return res            
                
sol = Solution()
test_data = [ [[],[]] , [[1,2,2,1],[2,2]], [[1,2,2,1],[1]], [[1,2,2,1],[2,3,4]] ,[[1],[1]]]
for d in test_data:
    print sol.intersect(d[0],d[1])
