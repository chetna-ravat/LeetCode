class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
    
   #    This question is similar to isomorphic string question
        
        k = s.split()
        if len(p) != len(k):
            return False
        # print(k)
        d = dict()
        e = dict()
        for i in range (0, len(p)):
            if p[i] not in d:
                d[p[i]] = k[i]
            elif d[p[i]] != k[i]:
                return False
        for i in range (0, len(k)):
            if k[i] not in e:
                e[k[i]] = p[i]
            elif e[k[i]] != p[i]:
                return False
        return True

s = Solution()
assert True == s.wordPattern("abba", "dog cat cat dog")
assert False == s.wordPattern("abba", "dog cat cat fish")
assert False == s.wordPattern("aaaa", "dog cat cat dog")