class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = s.split(" ")
        
        newlist = list()
        for i in new_s:
            l = list(i)
            n = len(i)- 1
            x = 0
            while x< n:
                swap = l[x]
                l[x] = l[n]
                l[n]= swap
                x +=1
                n-=1
            original = "". join(l)
            newlist.append(original)
        output = " ".join(newlist)
        
        # output = ""
        # for i in range(0,len(newlist)):
        #     output += newlist[i]
        #     if i < len(newlist) - 1:
        #         output += " "
           
        return output

s = Solution()

assert "s'teL ekat edoCteeL tsetnoc" == s.reverseWords("Let's take LeetCode contest")
assert "doG gniD" == s.reverseWords("God Ding")
