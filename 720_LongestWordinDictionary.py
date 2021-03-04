class Solution:
    def longestWord(self, words: List[str]) -> str:
        self.longestword = ""
        def dfs(idx,words):
            #print("idx",idx,words[idx])
            if idx == len(words):
                return
            idxlen = len(words[idx])
            for j in range(len(words)):
                #print("idx loop ",idx,words[j],words[j][0:idxlen])
                if idx!=j and words[j][0:idxlen] == words[idx] and len(words[j][idxlen:]) ==1:
                    #print(words[idx],words[j])
                    if len(words[j]) > len(self.longestword):
                        self.longestword = words[j]
                    dfs(j,words)
                
        words.sort()        
        i = 0        
        while i < len(words):
            if len(words[i]) == 1:
                #print("check",i)
                if self.longestword == "":
                    self.longestword = words[i]
                dfs(i,words)               
            i+=1
        
        return self.longestword
        
'''
["rac","rs","ra","on","r","otif","o","onpdu","rsf","rs","ot","oti","racy","onpd"]
["w","wo","wor","worl","world"]
["a", "banana", "app", "appl", "ap", "apply", "apple"]
["a","def"]
["z"]
["a","cd","cde"]
["n","j","sl","yyd","slo","jk","jkdt","y","yy"]
'''  

class Solution:
    def longestWord(self, words: List[str]) -> str:
        longestword = ""
        
        words.sort()        
        print(words)
        
        wordMap = {}
        
        for w in words:            
            flag = True
            if len(w) == 1:
                wordMap[w] = 1
                tmp = w
            else:                
                for i in range(1,len(w)):                
                    if wordMap.get(w[0:i]) == None:                        
                        flag=False                
                if flag:
                    wordMap[w]=1
            if len(w) > len(longestword) and flag==True:
                longestword = w
        
        return longestword   
        
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        longestword = ""
        
        words.sort()        
        #print(words)
        
        wordMap = ['']
        
        for w in words:
            if w[:-1] in wordMap:            
                wordMap.append(w)
                if len(w) > len(longestword) :
                    longestword = w
        
        return longestword        