from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m = len(languages)
        langmap = [0]
        friendflag = {}
        for l in languages:
            tmp = {}
            for nn in l:
                tmp[nn]=1
            langmap.append(tmp)

        cnt = 0
        teach_friendships = []
        for f in friendships:
            a = set(languages[f[0]-1])
            b = set(languages[f[1]-1])
            if len(a.intersection(b)) == 0:
                cnt+=1
                teach_friendships.append(f)
        for f in teach_friendships:
            friendflag[f[0]] = 1
            friendflag[f[1]] = 1
        #print("n",n,cnt,teach_friendships, friendflag)

        ans = -1

        for i in range(1,n+1): #lang
            cnt = 0
            for j in range(1,m+1): # users
                #print(i,j,langmap[j].get(i), friendflag.get(j))
                if langmap[j].get(i)==None and friendflag.get(j)!=None and friendflag[j]==1:
                    cnt+=1

            #print("cnt",cnt)
            if ans == -1:
                ans = cnt
            else:
                ans = min(cnt,ans)
        # langlist = languages to list

        # u 1 to n
        #   if u has friend:
        #       for lang not in languages[i]
        #           teach other people


        return ans

print(Solution().minimumTeachings( n = 12, languages = [[1,2],[1,2],[1,2]], friendships = [[1,2],[1,3],[2,3]]))
print(Solution().minimumTeachings( n = 5, languages = [[1],[2],[5],[5]], friendships = [[1,2],[3,4]]))
print(Solution().minimumTeachings( n = 5, languages = [[1],[2],[3],[4]], friendships = [[1,2],[3,4]]))
# print(Solution().minimumTeachings(  n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]))
# print(Solution().minimumTeachings(  n = 40, languages = [[1],[2],[1,3],[4]], friendships = [[1,2],[3,4]]))
# print(Solution().minimumTeachings(  n = 2, languages = [[1],[2]], friendships = [[1,2]]))

n = 11
languages = [[3,11,5,10,1,4,9,7,2,8,6],[5,10,6,4,8,7],[6,11,7,9],[11,10,4],[6,2,8,4,3],[9,2,8,4,6,1,5,7,3,10],[7,5,11,1,3,4],[3,4,11,10,6,2,1,7,5,8,9],[8,6,10,2,3,1,11,5],[5,11,6,4,2]]
friendships =[[7,9],[3,7],[3,4],[2,9],[1,8],[5,9],[8,9],[6,9],[3,5],[4,5],[4,9],[3,6],[1,7],[1,3],[2,8],[2,6],[5,7],[4,6],[5,8],[5,6],[2,7],[4,8],[3,8],[6,8],[2,5],[1,4],[1,9],[1,6],[6,7]]

print(Solution().minimumTeachings(  n = n, languages = languages, friendships = friendships))
#  n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]

# 1: 2 3
# 2: 3
#
# 1 1,3
# 2 2,3
#
#
# 1 2 3
# 2 1 3
# 3 2
