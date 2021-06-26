from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        import heapq
        claz = []
        for i,c in enumerate(classes):
            diff = (c[0]+1)/(c[1]+1) -  c[0]/c[1]
            claz.append((-diff,i,[(c[0]+1),(c[1]+1)]))
            #claz.append(-r)

        heapq.heapify(claz)
        #print(claz)
        for i in range(extraStudents):
            c = heapq.heappop(claz)
            pt = c[2]
            pnew = pt[0]+1
            tnew = pt[1]+1
            diff = pnew/tnew -  pt[0]/pt[1]
            classes[c[1]][0]+=1
            classes[c[1]][1]+=1
            heapq.heappush(claz, (-diff,c[1],[pnew,tnew]))
            #print(claz)
        #print(classes)

        ans = 0
        for c in classes:
            ans += c[0]/c[1]
        return ans/len(classes)

print(Solution().maxAverageRatio(classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4))
print(Solution().maxAverageRatio( classes = [[1,2],[3,5],[2,2]], extraStudents = 2))
