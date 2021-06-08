from typing import List

# class Solution:
#     def minOperations(self, boxes: str) -> List[int]:
#         ans = [ 0 for i in range(len(boxes))]
#
#         for i,c in enumerate(boxes):
#             if c == '1':
#                 for j in range(len(boxes)):
#                     ans[j] += abs(i-j)
#         return ans
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [ 0 for i in range(len(boxes))]
        cnt=0
        one=0
        for i in range(len(boxes)):
            ans[i]+=cnt
            if boxes[i]=='1':
                one+=1
            cnt+=one
        cnt=0
        one = 0
        for i in range(len(boxes)-1,-1,-1):
            ans[i]+=cnt
            if boxes[i]=='1':
                one += 1
            cnt += one
        return ans
print(Solution().minOperations(boxes = "001011"))
print(Solution().minOperations(boxes = "110"))
print(Solution().minOperations(boxes = "1"*1000))
print("1"*1000)