class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        print(len(a),len(b))
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
        def chkMax(targetMax,cntarr):
            cnt=0
            for i in range(256):
                if cntarr[i] > 0:
                    if i <= targetMax:
                        cnt += cntarr[i]
            return cnt
        def chkMin(targetMin,cntarr):
            cnt=0
            for i in range(256):
                if cntarr[i] > 0:
                    if i >= targetMin:
                        cnt += cntarr[i]
            return cnt

        amin,amax,acntarr = getMaxMin(a)
        bmin,bmax,bcntarr = getMaxMin(b)
        if amin == amax == bmax == bmin:
            return 0
        print(amin,amax,acntarr[97:])
        print(bmin,bmax,bcntarr[97:])

        achg = min(chkMin(bmin,acntarr),chkMax(bmax,acntarr))
        bchg = min(chkMin(amin,bcntarr),chkMax(amax,bcntarr))

        chgsame = 10000000
        for i in range(256):
            if acntarr[i] > 0 and bcntarr[i]> 0:
               chgsame = min(chgsame,len(a) - acntarr[i] +len(b) - bcntarr[i])

        print(achg)
        print(bchg)
        print(chgsame)
        minmax = max(acntarr[amin] + bcntarr[bmax], acntarr[amax] + bcntarr[bmin])
        print(minmax)
        return min(min(min(achg,bchg),chgsame),minmax)
#print(1733)
# print(Solution().minCharacters("ace","abe") == 2)
# print(Solution().minCharacters( a = "dabadd", b = "cda") == 3)
# print(Solution().minCharacters(  a = "aba", b = "caa") ==2)
# print(Solution().minCharacters(  a = "aa", b = "aaaaa") == 0)
# print(Solution().minCharacters(  a = "ae", b = "b")==1)
# print(Solution().minCharacters(  a = "aaaa", b = "aaab")==1)
# print(Solution().minCharacters(  a = "aaccccz", b = "aaeeeeeez")==3)
# print(Solution().minCharacters(  a = "aaccccd", b = "aaeeeeeez")==2)
#print(Solution().minCharacters(  a = "dbc", b = "daecc")==2)
print(Solution().minCharacters(  a = "jukdyrwxmayusovrggihfiluaewjbixpxybjfsjuyjcdnsxacodbwfdbfyklwfkblnijmhwivo",
                                 b = "sdtinjseqrjmmumheuimgmnwfjgwftdldjwpugupnwnltslplgufmynmsovqnculunfycwlxrcregkwkvlwwkhitqyiavabxhu")==69)


# #      a b c d e
# # ace  1   1   1
#        1 1 2 2 3
# # abe  1 1     1
#        1 2 2 2 3

