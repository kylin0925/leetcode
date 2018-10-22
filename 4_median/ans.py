class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
		m = len(nums1)
		n = len(nums2)
		i = 0
		j = 0
		ans = []
		while i < m or j < n:
			if i >= m:
				ans.append(nums2[j])
				j+=1
			elif j>=n:
				ans.append(nums1[i])
				i+=1
			elif nums1[i]<nums2[j]:
				ans.append(nums1[i])
				i+=1
			else:
				ans.append(nums2[j])
				j+=1
		ansLen = len(ans)
		print ans
		if ansLen%2 == 1:
			return float(ans[ansLen/2])
		else:
			tmp = ansLen/2
			return (ans[tmp-1]+ans[tmp])/2.0
		
a = Solution()

r = a.findMedianSortedArrays([1,2],[3,4])
print r == 2.5
r = a.findMedianSortedArrays([1,3],[2])
print r == 2.0

r = a.findMedianSortedArrays([1,3],[4,5])
print r == 3.5

r = a.findMedianSortedArrays([1,2,3],[1,2])
print r == 2.0