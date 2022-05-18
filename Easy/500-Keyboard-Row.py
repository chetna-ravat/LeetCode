class Solution:
    def findWords(self, words):
        s1 = set("qwertyuiop")
        s2 = set("asdfghjkl")
        s3 = set("zxcvbnm")
        l = list()
        
        for word in words:
            if word[0].lower() in s1:
                self.check(word,s1,l)
                
            elif word[0].lower() in s2:
                
                self.check(word,s2,l)
                
            elif word[0].lower() in s3:
                self.check(word,s3,l)
        return l
    
    
    
    def check(self,word,s,l):
        z = word.lower()
        for i in range(0, len(word)):
            if z[i] not in s:
                return None
       
        l.append(word) 
        
    
    
s = Solution()
words = ["Hello","Alaska","Dad","Peace"]
assert ["Alaska","Dad"] == s.findWords(words)

words = ["omk"]
assert [] == s.findWords(words)
