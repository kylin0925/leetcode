class Solution(object):
    @profile
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows <= 1:
            return s
          
        slen = len(s)
        if slen < numRows:
            return s
        #width
        block_width = numRows - 1
        block_size = numRows + numRows - 2
        blocks = slen/block_size+1
        row_size =  blocks * block_width
        
        #print row_size,slen
        
        ans = []
        
        ans  = [[""] * row_size for i in range(numRows)]
        #for i in ans:
        #    print i
        
        
        for b in range(blocks):       
            for y in range(numRows):
                
                if b*block_size+y < slen:
                    ans[y][b * block_width] = s[b*block_size+y]
                
                stmp = b*block_size + y +  (numRows - y - 1)*2
                xtmp = b*block_width + numRows - y - 1;
                #print "stmp " , stmp,"xtmp ",xtmp
                if b*block_size+y < slen:
                    if xtmp > 0 and stmp < slen and xtmp < row_size:                    
                        ans[y][xtmp] = s[stmp]
                #print ans[y]
            
        tmp = ""
        #print ans
        #print "---------------------"
        #for i in ans:           
        #    print "".join(i)
        for i in ans:
            tmp +="".join(i)
        #print tmp
        return tmp
a = Solution()

#n = a.convert("PAYPALISHIRING",3)
#print n == "PAHNAPLSIIGYIR"
n = a.convert("12",3)
print n == "12"
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


for i in range(1000):
    n = a.convert("dhkiqhukrzhozmyxznwkxolutcszdxdjfntxxphqooepdfpesloszbmvdgwjgzunonkncresikklpzpkkfclgqimwevcfprwebjivnadykqplhzvmdjuttgsadwfsobyplgkajpavfqhoreavpxojdijhfqbtscifivhtkipsawgrcjosgfblnmuseylwawdirledttvtremtpblxgoitcfmhdxfdtjnmwrqrmnmdtyxibkhhbsddxpmaosdkdswbkosweecxcbielrnojqsghgiwanidggesvyqbcsahtinhaavltpsawaywogcwniokhenjznquyfbyizlboddkgcjwklszvilcmymnmeikklkskvvzbylhcwfpjxoffchtctjoarakcmepizolzbucyztjwjodlwyorheryfddrjubkkmkliolhjvfsjiehhubqyupfauzjqawapilxyzhhumzfvfpezquaklhmhgwxjuxaclzakghgtilqocwpsqrfezrlhplqlksnvsnhywntfbjvdfkwycdedwpkocbznvnincsobfhigtdkaniarneujwfxyizldowtqqhtvqbeleoouyollviwrpwpxvdcjbxbrgvozwskdiaxgpktksqdhmsgjxluakvtrsiqrccwldtrudngydjhrdocdbwfltzeojuhlzdwewqabdibirjbwzdbczhnugsipopcpsbvqrvuwdvgwehvfkwhldvhlpqcfhfxcgsuzqovtkbsqknwwjdjnaqaridzsiwuoqongfkcpnuhxhftslchluifdlevvcrjufydkkhbxblwkqrebtmppwuuhapcegnaonfaxmewprsbhjgleuatqwoxyfbeoogedmgaykwobqrlzxwdryyhwogwujaiziocuuevhalkscv",700)
    print n == ""


n = a.convert("pdhoozufbkgswhmwruzpdfgysycpvmwlrfzfevkhitagaoctiejnlrodpqskeqxvwzccwpkekmkmapgltryeimjzeblirjfpkksgzeljqxvsmddhueleswdxxrhrapgmzasaeflwdippmuxiykpthssgjzzlqgxrisrnxelanaszxrjxdyqmtiteksqaapsljlahqljdodeluniamzmhhhltcduevopebpnrdzwrcaczqmzelnlvvwozakdvyvbakptpoqgqskrixqmkezfbwwaygfthauhnlcczsjsnvjvsakdgjkjhglfpqawrxfeijiietcrplmhnymvixepfpvwivuzsbfdlnnpjpgyaufotslbrqsyhpvpnpohrvkclxtumzsptzfmtqpkgkjqzefmvwumteqeejaskuheumsndkalulbtrhimfczyirdmdffnaotwbmlgyltsyvnpevclxdjiuowxudnwsgsvufdsrwkrtahzvjkvoudikbiefvaxduuyaxqtvdkpdtqacbvqxabhclohiqgllcjnzciwfulkockqfgjcimlkxztfqbsddeqeiybnsozgsjzzrkdawpmtqiaglujrabxibyxwpwejgfjxpmzlboguwiahfmafpyorylpnitxqzipoupcyfisbtukyildyjtrhhgxpzwhyewpanrasbstupguxtavevmncsktui",503)
print n == ""
