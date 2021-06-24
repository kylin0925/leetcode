from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        g = {}

        for e in edges:
            n = g.get(e[0], 0)
            n += 1
            g[e[0]] = n
            n = g.get(e[1], 0)
            n += 1
            g[e[1]] = n

        for k in g.keys():
            if g[k] == len(g.keys())-1:
                return k
        return 0


class Solution1:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] in edges[1]:
            return edges[0][0]

        if edges[0][1] in edges[1]:
            return edges[0][1]


class Solution2:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]

        if edges[0][1] == edges[1][0] or edges[0][1] == edges[1][1]:
            return edges[0][1]


class Solution3:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] in edges[1]:
            return edges[0][0]

        return edges[0][1]
print(Solution3().findCenter( [[1,2],[2,3],[4,2]]))
print(Solution3().findCenter( edges = [[1,2],[5,1],[1,3],[1,4]]))