class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        i = len(a)-1
        j = len(b)-1
        
        l = list()
        
        sum = 0
        carry = 0
        while i >=0 or j >=0 :
            sum = carry
            if i >= 0:
                sum += int(a[i])
            if j >= 0:
                sum += int(b[j])
                
                
                
            # if i < 0:
            #     sum = carry + int(b[j])
            # elif j < 0:
            #     sum = carry + int(a[i])
            # else:
            #     sum = carry + int(a[i]) + int(b[j])
            
            if sum == 2:
                sum = 0
                carry = 1
            elif sum == 3:
                sum = 1
                carry = 1
            else:
                carry = 0
            l.append(str(sum))
            i-=1
            j-=1
        if carry == 1:
            l.append(str(carry))
        
        l.reverse()
        output = "".join(l)
        return output
        
        

s = Solution()
assert "100" == s.addBinary("11", "1")
assert "10101" == s.addBinary("1010", "1011")
assert "110" == s.addBinary("11", "11")
