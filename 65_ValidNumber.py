class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        print("test",s)
        state = 0
        INTEGER = 1
        INT_FLOAT = 2
        EXP = 3
        INT_FLOAT = 4
        INT_FLOAT_NUM = 5
        FLOAT = 6
        FLOAT_NUM = 7
        SIGN = 8
        EXP_NUM = 9
        EXP_SIGN = 10
        if len(s) == 0:
            return False
        for c in s:
            if state == 0:
                if c == '+' or c == '-':
                    state = SIGN
                elif c.isdigit():
                    state = INTEGER
                elif c == '.':
                    state = FLOAT
                else:
                    return False
            elif state ==SIGN:
                if c.isdigit():
                    state = INTEGER
                elif c == '.':
                    state = FLOAT
                else:
                    return False
            elif state == INTEGER:
                if c.isdigit():
                    continue
                elif c == '.':
                    state = INT_FLOAT
                elif c == 'e':
                    state = EXP
                else:
                    return False
            elif state == INT_FLOAT:
                if c.isdigit():
                    state = INT_FLOAT_NUM
                elif c == 'e':
                    state = EXP
                else:
                    return False
            elif state == INT_FLOAT_NUM:
                if c.isdigit():
                    continue
                elif c == 'e':
                    state = EXP
                else:
                    return False
            elif state == EXP:
                if c == '+' or c == '-':
                    state = EXP_SIGN
                elif c.isdigit():
                    state = EXP_NUM
                else:
                    return False
            elif state == EXP_NUM:
                if c.isdigit():
                    continue
                else:
                    return False
            elif state == EXP_SIGN:
                if c.isdigit():
                    state = EXP_NUM
                else:
                    return False
            elif state == FLOAT:
                if c.isdigit():
                    state = FLOAT_NUM
                else:
                    return False
            elif state == FLOAT_NUM:
                if c.isdigit():
                    continue
                elif c == 'e':
                    state = EXP
                else:
                    return False
        if state == SIGN or state == EXP or state == FLOAT or state == EXP_SIGN:
            return  False
        else:
            return True

sol = Solution()
# print(sol.isNumber("0") == True)
# print(sol.isNumber("2e10") == True)
# print(sol.isNumber("53.5e93") == True)
# print(sol.isNumber(" 0.1 ") == True)
# print(sol.isNumber(" -90e3   ") == True)
# print(sol.isNumber("1 a") == False)
# print(sol.isNumber("-+3") == False)
# print("-"*30)
# print(sol.isNumber("-3"))
# print(sol.isNumber("-31.0e-19"))
print(sol.isNumber("46.e-19"))
print(sol.isNumber("1e"))
print(sol.isNumber("1e1.888"))
print(sol.isNumber("1e-1.888"))
print(sol.isNumber("+11111.999e-1"))
print(sol.isNumber("+abcde-1"))
print(sol.isNumber("-1 111"))
print(sol.isNumber("-1 .111"))
print(sol.isNumber(" .111"))
print(sol.isNumber(" .111e123     "))
print(sol.isNumber(" .111e123     "))
print(sol.isNumber(" +     "))
print(sol.isNumber(" -e     "))
print(sol.isNumber(" -e1     "))
print(sol.isNumber(" -.e1     "))
print(sol.isNumber(" .     "))
print(sol.isNumber("      "))
print(sol.isNumber(" 10e+     "))
