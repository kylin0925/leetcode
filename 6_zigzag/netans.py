class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows==1: return s
        tmp=['' for i in range(nRows)]
        index=-1; step=1
        for i in range(len(s)):
            index+=step
            if index==nRows:
                index-=2; step=-1
            elif index==-1:
                index=1; step=1
            tmp[index]+=s[i]
        return ''.join(tmp)
a = Solution()

#n = a.convert("PAYPALISHIRING",3)
#print n == "PAHNAPLSIIGYIR"
   
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



n = a.convert("dhkiqhukrzhozmyxznwkxolutcszdxdjfntxxphqooepdfpesloszbmvdgwjgzunonkncresikklpzpkkfclgqimwevcfprwebjivnadykqplhzvmdjuttgsadwfsobyplgkajpavfqhoreavpxojdijhfqbtscifivhtkipsawgrcjosgfblnmuseylwawdirledttvtremtpblxgoitcfmhdxfdtjnmwrqrmnmdtyxibkhhbsddxpmaosdkdswbkosweecxcbielrnojqsghgiwanidggesvyqbcsahtinhaavltpsawaywogcwniokhenjznquyfbyizlboddkgcjwklszvilcmymnmeikklkskvvzbylhcwfpjxoffchtctjoarakcmepizolzbucyztjwjodlwyorheryfddrjubkkmkliolhjvfsjiehhubqyupfauzjqawapilxyzhhumzfvfpezquaklhmhgwxjuxaclzakghgtilqocwpsqrfezrlhplqlksnvsnhywntfbjvdfkwycdedwpkocbznvnincsobfhigtdkaniarneujwfxyizldowtqqhtvqbeleoouyollviwrpwpxvdcjbxbrgvozwskdiaxgpktksqdhmsgjxluakvtrsiqrccwldtrudngydjhrdocdbwfltzeojuhlzdwewqabdibirjbwzdbczhnugsipopcpsbvqrvuwdvgwehvfkwhldvhlpqcfhfxcgsuzqovtkbsqknwwjdjnaqaridzsiwuoqongfkcpnuhxhftslchluifdlevvcrjufydkkhbxblwkqrebtmppwuuhapcegnaonfaxmewprsbhjgleuatqwoxyfbeoogedmgaykwobqrlzxwdryyhwogwujaiziocuuevhalkscv",700)
print n == ""


n = a.convert("pdhoozufbkgswhmwruzpdfgysycpvmwlrfzfevkhitagaoctiejnlrodpqskeqxvwzccwpkekmkmapgltryeimjzeblirjfpkksgzeljqxvsmddhueleswdxxrhrapgmzasaeflwdippmuxiykpthssgjzzlqgxrisrnxelanaszxrjxdyqmtiteksqaapsljlahqljdodeluniamzmhhhltcduevopebpnrdzwrcaczqmzelnlvvwozakdvyvbakptpoqgqskrixqmkezfbwwaygfthauhnlcczsjsnvjvsakdgjkjhglfpqawrxfeijiietcrplmhnymvixepfpvwivuzsbfdlnnpjpgyaufotslbrqsyhpvpnpohrvkclxtumzsptzfmtqpkgkjqzefmvwumteqeejaskuheumsndkalulbtrhimfczyirdmdffnaotwbmlgyltsyvnpevclxdjiuowxudnwsgsvufdsrwkrtahzvjkvoudikbiefvaxduuyaxqtvdkpdtqacbvqxabhclohiqgllcjnzciwfulkockqfgjcimlkxztfqbsddeqeiybnsozgsjzzrkdawpmtqiaglujrabxibyxwpwejgfjxpmzlboguwiahfmafpyorylpnitxqzipoupcyfisbtukyildyjtrhhgxpzwhyewpanrasbstupguxtavevmncsktui",503)
print n == ""