class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.withSort(s,t)
        
    def withHashMap(self, s: str, t: str) :
        d = dict()
        for i in s:
            if i not in d:
                d[i]= 1
            else:
                d[i]+=1
        for i in t:
            if i in d:
                d[i] -=1
            else:
                return False
        for value in d.values():
            if value !=0:
                return False
        return True

    
    def withSort(self, s: str, t: str) :
        if len(s) != len(t):
            return False
        
        
        l1 = list(s)
        l2 = list(t)
            
        l1.sort()
        l2.sort()
        for i in range (0, len(l1)):
            if l1[i] != l2[i]:
                return False
        return True
    

s = Solution()
assert True == s.isAnagram("anagram", "nagaram")
assert False == s.isAnagram("rat", "cat")