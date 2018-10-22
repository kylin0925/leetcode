symbol = [  
            ["M","MM","MMM"],
            ["C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
            ["X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
            ["I","II","III","IV","V","VI","VII","VIII","IX"],
            ]
number = [  
            [1000,2000,3000]    ,        
            [ 100, 200, 300,400,500,600,700,800,900],
            [  10,  20,  30, 40, 50, 60, 70, 80, 90],
            [   1,2,3,4,5,6,7,8,9],
            ]          
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        i = 0;
        res = []
        to_int = 0
        x = 0
        m_x=0
        y = 0
        for p in symbol:
            match = ""
            for roman in p:
                len_rom = len(roman)
                #print i,i+len_rom, s[i:i+len_rom]
                if s[i:i+len_rom] == roman:
                    match = s[i:i+len_rom]
                    m_x = x        
                x+=1
            if match !="":
                #res.append(match)
                #print y,m_x
                to_int += number[y][m_x]
                
            i+=len(match)
            y+=1
            x = 0
            
        return to_int
s = Solution();
s.romanToInt("II")
s.romanToInt("III")
s.romanToInt("IV")
s.romanToInt("IX")
s.romanToInt("XX")
s.romanToInt("C")
s.romanToInt("CDI")
s.romanToInt("DCXXI")
