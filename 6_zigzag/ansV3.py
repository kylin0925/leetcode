class Solution(object):
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
        
        ans  = ["" for i in range(numRows)]
        #print ans      
        x = 0 
        y = 0
        dir = 1
        for i in range(slen):
        
            ans [y] += s[i]
            if y <= 0:           
                dir =1
            elif y >=(numRows-1):
                dir=-1                
            
            y+=dir
        tmp = ""

        for i in ans:
            tmp +="".join(i)
        #print tmp
        return tmp
a = Solution()

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

for i in range(1000):
    n = a.convert("dhkiqhukrzhozmyxznwkxolutcszdxdjfntxxphqooepdfpesloszbmvdgwjgzunonkncresikklpzpkkfclgqimwevcfprwebjivnadykqplhzvmdjuttgsadwfsobyplgkajpavfqhoreavpxojdijhfqbtscifivhtkipsawgrcjosgfblnmuseylwawdirledttvtremtpblxgoitcfmhdxfdtjnmwrqrmnmdtyxibkhhbsddxpmaosdkdswbkosweecxcbielrnojqsghgiwanidggesvyqbcsahtinhaavltpsawaywogcwniokhenjznquyfbyizlboddkgcjwklszvilcmymnmeikklkskvvzbylhcwfpjxoffchtctjoarakcmepizolzbucyztjwjodlwyorheryfddrjubkkmkliolhjvfsjiehhubqyupfauzjqawapilxyzhhumzfvfpezquaklhmhgwxjuxaclzakghgtilqocwpsqrfezrlhplqlksnvsnhywntfbjvdfkwycdedwpkocbznvnincsobfhigtdkaniarneujwfxyizldowtqqhtvqbeleoouyollviwrpwpxvdcjbxbrgvozwskdiaxgpktksqdhmsgjxluakvtrsiqrccwldtrudngydjhrdocdbwfltzeojuhlzdwewqabdibirjbwzdbczhnugsipopcpsbvqrvuwdvgwehvfkwhldvhlpqcfhfxcgsuzqovtkbsqknwwjdjnaqaridzsiwuoqongfkcpnuhxhftslchluifdlevvcrjufydkkhbxblwkqrebtmppwuuhapcegnaonfaxmewprsbhjgleuatqwoxyfbeoogedmgaykwobqrlzxwdryyhwogwujaiziocuuevhalkscv",700)
    print n == ""


n = a.convert("pdhoozufbkgswhmwruzpdfgysycpvmwlrfzfevkhitagaoctiejnlrodpqskeqxvwzccwpkekmkmapgltryeimjzeblirjfpkksgzeljqxvsmddhueleswdxxrhrapgmzasaeflwdippmuxiykpthssgjzzlqgxrisrnxelanaszxrjxdyqmtiteksqaapsljlahqljdodeluniamzmhhhltcduevopebpnrdzwrcaczqmzelnlvvwozakdvyvbakptpoqgqskrixqmkezfbwwaygfthauhnlcczsjsnvjvsakdgjkjhglfpqawrxfeijiietcrplmhnymvixepfpvwivuzsbfdlnnpjpgyaufotslbrqsyhpvpnpohrvkclxtumzsptzfmtqpkgkjqzefmvwumteqeejaskuheumsndkalulbtrhimfczyirdmdffnaotwbmlgyltsyvnpevclxdjiuowxudnwsgsvufdsrwkrtahzvjkvoudikbiefvaxduuyaxqtvdkpdtqacbvqxabhclohiqgllcjnzciwfulkockqfgjcimlkxztfqbsddeqeiybnsozgsjzzrkdawpmtqiaglujrabxibyxwpwejgfjxpmzlboguwiahfmafpyorylpnitxqzipoupcyfisbtukyildyjtrhhgxpzwhyewpanrasbstupguxtavevmncsktui",503)
print n == ""
