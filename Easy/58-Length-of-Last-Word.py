class Solution:
    
    def lengthOfLastWord(self, s: str) -> int:
        return self.useSwitch(s)
    
    def useCounter(self, s):
        counter = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                counter +=1
            elif s[i] == " " and counter > 0:
                break
            else:
                pass
        return counter
    
    def useSwitch(self,s: str):
        isWordSeen = False
        counter = 0
        for i in range (len(s)-1, -1,-1):
            if s[i] != " ":
                counter +=1
                isWordSeen = True
            elif isWordSeen == True:
                break
        return counter
    
s = Solution()
assert 5 == s.lengthOfLastWord("Hello World")
assert 4 == s.lengthOfLastWord("   fly me   to   the moon  ")
assert 6 == s.lengthOfLastWord("luffy is still joyboy")
assert 0 == s.lengthOfLastWord("")
assert 0 == s.lengthOfLastWord("                                     ")