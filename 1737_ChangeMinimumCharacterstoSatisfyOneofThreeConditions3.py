class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        lena = len(a)
        lenb = len(b)
        def Count(s):
            cntarr = [ 0 for i in range(256)]
            accarr = [ 0 for i in range(256)]
            for c in s:
                cin = ord(c)
                cntarr[cin]+=1

            for i in range(1,256):
                accarr[i]+=cntarr[i]+accarr[i-1]

            return cntarr,accarr


        acntarr,acca = Count(a)
        bcntarr,accb = Count(b)

        #print(acntarr[97:97+26],acca[97:97+26])
        #print(bcntarr[97:97+26],accb[97:97+26])

        chgsame = 10000000
        for i in range(256):
            if acntarr[i] > 0 and bcntarr[i]> 0:
               chgsame = min(chgsame,len(a) - acntarr[i] +len(b) - bcntarr[i])
        achg = 1000000
        for i in range(97,97+25):
            #if acntarr[i] > 0 :
                achg = min(achg, lena - acca[i] + accb[i])
                #print("a",lena - acca[i] + accb[i])
        for i in range(97,97+25):
            #if bcntarr[i] > 0 :
                achg = min(achg, lenb - accb[i] + acca[i])
                #print("b",lenb - accb[i] + acca[i])
        #print(achg,chgsame)
        return min(achg,chgsame)
#print(1733)
print(Solution().minCharacters("qxbzazzh","x") == 2)
print(Solution().minCharacters("a","abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 2)
print(Solution().minCharacters("ace","abe") == 2)
print(Solution().minCharacters( a = "dabadd", b = "cda") == 3)
print(Solution().minCharacters(  a = "aba", b = "caa") ==2)
print(Solution().minCharacters(  a = "aa", b = "aaaaa") == 0)
print(Solution().minCharacters(  a = "ae", b = "b")==1)
print(Solution().minCharacters(  a = "aaaa", b = "aaab")==1)
print(Solution().minCharacters(  a = "aaccccz", b = "aaeeeeeez")==3)
print(Solution().minCharacters(  a = "aaccccd", b = "aaeeeeeez")==2)
print(Solution().minCharacters(  a = "dbc", b = "daecc")==3)
print(Solution().minCharacters(  a = "jukdyrwxmayusovrggihfiluaewjbixpxybjfsjuyjcdnsxacodbwfdbfyklwfkblnijmhwivo",
                                 b = "sdtinjseqrjmmumheuimgmnwfjgwftdldjwpugupnwnltslplgufmynmsovqnculunfycwlxrcregkwkvlwwkhitqyiavabxhu")==69)
#


"x"
# #      a b c d e
# # ace  1   1   1
#        1 1 2 2 3
# # abe  1 1     1
#        1 2 2 2 3

