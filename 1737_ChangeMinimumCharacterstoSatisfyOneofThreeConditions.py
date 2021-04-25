class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        amin = 27
        bmin = 27
        amax = -1
        bmax = -1

        def getMaxMin(s):
            smin =256
            smax =-1
            cntarr = [ 0 for i in range(256)]
            for c in s:
                cin = ord(c)
                if cin <smin:
                    smin = cin
                if ord(c) >smax:
                    smax = cin
                cntarr[cin]+=1
            return smin,smax,cntarr
        amin,amax,acntarr = getMaxMin(a)
        bmin,bmax,bcntarr = getMaxMin(b)
        if amin == amax == bmax == bmin:
            return 0
        print(amin,amax,acntarr)
        print(bmin,bmax,bcntarr)

        achg = 0
        bchg = 0

        for i in range(256):
            if acntarr[i]>0:
                if bmin <= i <= bmax:
                    achg+=acntarr[i]
        for i in range(256):
            if bcntarr[i] > 0:
                if amin <= i <= amax:
                    bchg+=bcntarr[i]
        print(achg)
        print(bchg)
        return min(achg,bchg)
#print(1733)
# print(Solution().minCharacters("abaa","abc"))
# print(Solution().minCharacters( a = "dabadd", b = "cda"))
# print(Solution().minCharacters(  a = "aba", b = "caa"))
# print(Solution().minCharacters(  a = "aa", b = "aaaaa"))
print(Solution().minCharacters(  a = "ae", b = "b"))
print(Solution().minCharacters(  a = "jukdyrwxmayusovrggihfiluaewjbixpxybjfsjuyjcdnsxacodbwfdbfyklwfkblnijmhwivo",
                                 b = "sdtinjseqrjmmumheuimgmnwfjgwftdldjwpugupnwnltslplgufmynmsovqnculunfycwlxrcregkwkvlwwkhitqyiavabxhu")==69)
