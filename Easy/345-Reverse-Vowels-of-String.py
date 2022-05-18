class Solution:
    def reverseVowels(self, value: str) -> str:
        return self.solution3(value)
    
    def solution1(self, value: str) -> str:
        s = list(value)
        l = set(['a', 'e','i','o','u','A','E','I',"O","U"])

        vowel = list()
        for i in range(0, len(s)):
            if s[i] in l:
                vowel.append(s[i])
                s[i] = "*"
        
        n = len(vowel)-1
        for i in range(0, len(s)):
            if s[i] == "*":
                s[i] = vowel[n]
                n-=1
        t = "". join(s)
        return t 
    
    def solution2(self, value: str) -> str:
        s = list(value)
        l = set(['a', 'e','i','o','u','A','E','I',"O","U"])
    
        i = 0
        n = len(s) -1
        while i < n:
            if s[i] in l:
                swap = s[i]
                while n >= i and s[n] not in l:
                    n -=1
                s[i] = s[n]
                s[n] = swap
                n -=1
            i +=1
        t = "". join(s)
        return t    
    
    def solution3(self, value: str) -> str:
        s = list(value)
        l = set(['a', 'e','i','o','u','A','E','I',"O","U"])
    
        i = 0
        n = len(s) -1
        while i < n:
            while i < len (s) and s[i] not in l:
                i +=1
            while n >= 0 and s[n] not in l:
                n -=1
            if i < n :
                swap = s[i]
                s[i] = s[n]
                s[n] = swap
                i += 1
                n -=1
        t = "". join(s)
        return t   
        
        
s = Solution()

assert "holle" == s.reverseVowels("hello")
assert "leotcede" == s.reverseVowels("leetcode")
