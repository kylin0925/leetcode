class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        slen = len(s)
        #width
        x = numRows - 1
        u = x * 2
        w = (slen/u+1) * x
        
        ans  = [["" for x in range(w)] for i in range(numRows)]
        #for i in ans:
        #    print "".join(i)
        j = 0
        i = 0
        while i < slen:
            ii = j * x
            #print "i ",i," ii ",ii
            for x in range(numRows):
            
                if i >= slen:

                    break
                ans[x][ii] = s[i]
                i+=1
                
            xx = ii + 1
                        
            for y in range(numRows-2,0,-1):
                #print "xx ",xx," y ",y," i ",i
                if i >= slen:
                    break
                ans[y][xx] = s[i]
                i+=1
                xx+=1
            
            j+=1
            
        tmp = ""
        #print ans
        for i in ans:
            for j in i:
                if j != "":
                    tmp +=j
        #print tmp
        return tmp
a = Solution()
'''
n = a.convert("PAYPALISHIRING",3)
print n == "PAHNAPLSIIGYIR"
   
n = a.convert("abcdef",1)
print n == "abcdef"
n = a.convert("abcdef",2)
print n == "acebdf" 
n = a.convert("abcdef",3)
print n == "aebdfc" 
n = a.convert("abcdef",4)
print n == "abfced" 
n = a.convert("abcdef12345",5)
print n == "a3b24c15dfe" 
'''


n = a.convert("dhkiqhukrzhozmyxznwkxolutcszdxdjfntxxphqooepdfpesloszbmvdgwjgzunonkncresikklpzpkkfclgqimwevcfprwebjivnadykqplhzvmdjuttgsadwfsobyplgkajpavfqhoreavpxojdijhfqbtscifivhtkipsawgrcjosgfblnmuseylwawdirledttvtremtpblxgoitcfmhdxfdtjnmwrqrmnmdtyxibkhhbsddxpmaosdkdswbkosweecxcbielrnojqsghgiwanidggesvyqbcsahtinhaavltpsawaywogcwniokhenjznquyfbyizlboddkgcjwklszvilcmymnmeikklkskvvzbylhcwfpjxoffchtctjoarakcmepizolzbucyztjwjodlwyorheryfddrjubkkmkliolhjvfsjiehhubqyupfauzjqawapilxyzhhumzfvfpezquaklhmhgwxjuxaclzakghgtilqocwpsqrfezrlhplqlksnvsnhywntfbjvdfkwycdedwpkocbznvnincsobfhigtdkaniarneujwfxyizldowtqqhtvqbeleoouyollviwrpwpxvdcjbxbrgvozwskdiaxgpktksqdhmsgjxluakvtrsiqrccwldtrudngydjhrdocdbwfltzeojuhlzdwewqabdibirjbwzdbczhnugsipopcpsbvqrvuwdvgwehvfkwhldvhlpqcfhfxcgsuzqovtkbsqknwwjdjnaqaridzsiwuoqongfkcpnuhxhftslchluifdlevvcrjufydkkhbxblwkqrebtmppwuuhapcegnaonfaxmewprsbhjgleuatqwoxyfbeoogedmgaykwobqrlzxwdryyhwogwujaiziocuuevhalkscv",700)
print n == ""